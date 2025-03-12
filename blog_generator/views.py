from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import json
from pytube import YouTube
import os
import assemblyai as aai
import openai
from .models import BlogPost
from openai import OpenAI
import os
import json
import yt_dlp
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# authentication views
@login_required
def index(request):
    return render(request, 'blog_generator/index.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'blog_generator/login.html', {'error_message': error_message})
        
    return render(request, 'blog_generator/login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_mesage = 'Error creating account'
                return render(request, 'blog_generator/signup.html', {'error_message' : error_mesage})
        else:
            error_mesage = 'Password do not match'
            return render(request, 'blog_generator/signup.html', {'error_message' : error_mesage})
    return render(request, 'blog_generator/signup.html')



# Configure Google Gemini API
genai.configure(api_key="AIzaSyDz42O41grhYr_ruSAwHTHKfwJrgShZoOk")


def youtube_title(link):
    """Extracts the title of the YouTube video."""
    try:
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=False)
            return info.get('title', 'Title not found')
    except Exception as e:
        return f"Error: {str(e)}"



def download_audio(youtube_link):
    """Downloads audio from YouTube and ensures the filename is correct."""
    try:
        # Extract a clean video ID (only the first 11 characters)
        video_id = youtube_link.split("/")[-1].split("?")[0]  # Removes `?si=...`
        output_filename = f"{video_id}.mp3"  # Clean filename

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': "%(id)s.%(ext)s",  # Forces ID-based naming
            'noplaylist': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_link, download=True)
            downloaded_filename = f"{info['id']}.mp3"

        return downloaded_filename if os.path.exists(downloaded_filename) else None

    except Exception as e:
        print(f"Download Error: {e}")  # Debugging
        return None




# Set up AssemblyAI API key
aai.settings.api_key = "046f81d7887149eba115864b2e76a72e"  # Replace with your actual API key

def get_transcription(youtube_link):
    audio_file = download_audio(youtube_link)

    if audio_file is None or not os.path.exists(audio_file):
        print("❌ Error: Audio file not found.")
        return "Error: Audio file not found."

    print(f"✅ Audio File Exists: {audio_file}")  # Debugging

    try:
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_file)  # Transcribe audio
        print(f"✅ Transcription: {transcript.text}")  # Debugging
        return transcript.text
    except Exception as e:
        print(f"❌ Transcription Error: {str(e)}")  # Debugging
        return f"Error: {str(e)}"


import google.generativeai as genai

genai.configure(api_key="AIzaSyDz42O41grhYr_ruSAwHTHKfwJrgShZoOk")

models = genai.list_models()
for model in models:
    print(model.name)


def generate_blog_from_transcription(transcription):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(f"Write a blog based on this transcription in proper structured way: {transcription}")

        print(f"✅ Blog Response: {response.text}")  # Debugging
        return response.text if response else "Blog generation failed."

    except Exception as e:
        print(f"❌ Blog Generation Error: {str(e)}")  # Debugging
        return f"Error: {str(e)}"


@csrf_exempt
def generate_blog(request):
    """Handles API requests for generating blogs from YouTube videos."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            youtube_link = data.get("link")

            if not youtube_link:
                return JsonResponse({"error": "No YouTube link provided"}, status=400)

            # Get YouTube video title
            title = youtube_title(youtube_link)

            # Get transcription
            transcription = get_transcription(youtube_link)
            if "Error" in transcription:
                return JsonResponse({"error": "Failed to get transcript"}, status=500)

            # Generate blog
            blog_content = generate_blog_from_transcription(transcription)
            if "Error" in blog_content:
                return JsonResponse({"error": "Failed to generate blog"}, status=500)

            return JsonResponse({"content": blog_content})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
    

    
def blog_list(request):
    blog_articles = BlogPost.objects.filter(user= request.user)
    return render(request, 'blog_generator/all-blogs.html', {'blog_articles' : blog_articles})

def blog_details(request, pk):
    blog_article_detail = BlogPost.objects.get(id = pk)
    if request.user == blog_article_detail.user:
        return render(request, 'blog_generator/blog-details.html', {'blog_article_detail' : blog_article_detail})
    else:
        return redirect('/')