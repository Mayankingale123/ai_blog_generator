# ai_blog_generator
Welcome to the AI-Powered YouTube Video Summarizer! This web application leverages cutting-edge technologies to provide users with AI-generated blog posts summarizing the content of YouTube videos. Our stack includes Django for web development ,yt_dlp ,AssemblyAI, OpenAI, google gmini for blog post generation.

Introduction
Welcome to the AI-Powered YouTube Video Summarizer! This web application leverages cutting-edge technologies to provide users with AI-generated blog posts summarizing the content of YouTube videos. Our stack includes Django for web development,yt_dlp for downloading audio from youtube link, AssemblyAI for video transcription, and OpenAI for blog post generation.

Key Features
Sleek Frontend: The frontend is designed with HTML and TailwindCSS, javascript, ensuring an appealing and user-friendly interface.

blogailogin

User Authentication: We've implemented a robust authentication system for user registration and login.

blogairegister

Seamless User Experience: JavaScript and Ajax integration make using our app a breeze.

blogaihomepage

Video Transcription: AssemblyAI transcribes YouTube videos for accurate content analysis.

AI-Generated Blogs: OpenAI generates insightful blog posts from video transcriptions.

allblogpost

Data Persistence: Blog posts are securely saved to the database for easy retrieval.

BlogpostDetails

Installation
Follow these steps to get your AI-Powered YouTube Video Summarizer up and running:

Clone this repository to your local machine.
git clone 'https://github.com/Mayankingale123/ai_blog_generator'

Set up a virtual environment and install the required packages listed in requirements.txt.
pip install 'requirements.txt'

Configure Django settings, including database configuration although I have used the default database of django dbsquillite.
Apply migrations and create a superuser for administrative access.
python manage.py createsuperuser

Obtain API keys for AssemblyAI and googel gemini and configure them within the application you can use open ai also but I have used google gemini instead.
Start the Django development server.
python manage.py runserver

Usage
Getting started with our application is straightforward:

Register and log in to your account.
Input a YouTube video link of your choice.
The application will transcribe the video and generate a blog post summarizing its content.
Save the blog post for future reference.
Explore your saved blog posts in your account.
Technologies Utilized
I harness the power of various technologies to deliver this functionality:

Django
HTML
TailwindCSS
JavaScript
Ajax
AssemblyAI
OpenAI
Future Enhancements
Our commitment to continuous improvement means I have plans for the following:

Implement user profiles for personalized experiences.
Enhance the UI/UX for a polished appearance.
Continuously improve summarization accuracy and AI-generated content.
Notes
During development, I used the free resources of AssemblyAI and google gemini. 
Warning
Please be mindful of potential issues:

Ensure that you do not exceed the token limit of the OpenAI or gemini ai API key.
Be aware that the free services of AssemblyAI may have limitations.
Contributing
I welcome contributions from the community. Feel free to submit issues or pull requests to help me improve.

Acknowledgments
I extend our gratitude to AssemblyAI and OpenAI and google gemini for providing powerful AI services that make this project possible.


