**# ai_blog_generator**


Introduction
Welcome to the AI-Powered YouTube Video Summarizer! This web application leverages cutting-edge technologies to provide users with AI-generated blog posts summarizing the content of YouTube videos. Our stack includes Django for web development,yt_dlp for downloading audio from youtube link, AssemblyAI for video transcription, and OpenAI for blog post generation.

## Key Features
- **Sleek Frontend**: The frontend is designed with HTML and TailwindCSS, ensuring an appealing and user-friendly interface.
  <br><br>
  ![image](https://github.com/user-attachments/assets/b41dbded-0d7b-4284-9175-b14a94d54494)




- **User Authentication**: We've implemented a robust authentication system for user registration and login.
  <br><br>
  ![image](https://github.com/user-attachments/assets/0d574131-3683-4f59-b314-62659cd7519e)



- **Seamless User Experience**: JavaScript and Ajax integration make using our app a breeze.
  <br><br>
![blogaihomepage](https://github.com/Abhay-Kanwasi/AI-Blog-Generator/assets/78997764/90d98beb-a34a-4a12-8d74-6dd415b1c5f1)


- **Video Transcription**: AssemblyAI transcribes YouTube videos for accurate content analysis.

- **AI-Generated Blogs**: OpenAI generates insightful blog posts from video transcriptions.
  <br><br>
![allblogpost](https://github.com/Abhay-Kanwasi/AI-Blog-Generator/assets/78997764/c40f81a0-de1d-4f70-8ae9-f34759de250d)

- **Data Persistence**: Blog posts are securely saved to the database for easy retrieval.
  <br><br>
![BlogpostDetails](https://github.com/Abhay-Kanwasi/AI-Blog-Generator/assets/78997764/07fd5081-9578-4628-bfc1-ebcc11ea4096)

## Installation
Follow these steps to get your AI-Powered YouTube Video Summarizer up and running:

1. Clone this repository to your local machine.
   > git clone 'https://github.com/Mayankingale123/ai_blog_generator'
3. Set up a virtual environment and install the required packages listed in `requirements.txt`.
   > pip install 'requirements.txt'
4. Configure Django settings, including database configuration.
5. Apply migrations and create a superuser for administrative access.
   > python manage.py createsuperuser
7. Obtain API keys for AssemblyAI and OpenAI and configure them within the application.
8. Start the Django development server.
   > python manage.py runserver

## Usage
Getting started with our application is straightforward:

1. Register and log in to your account.
2. Input a YouTube video link of your choice.
3. The application will transcribe the video and generate a blog post summarizing its content.
4. Save the blog post for future reference.
5. Explore your saved blog posts in your account.

## Technologies Utilized
I harness the power of various technologies to deliver this functionality:

- Django
- HTML
- TailwindCSS
- JavaScript
- Ajax
- AssemblyAI
- OpenAI
- google gemini
**Implement user profiles for personalized experiences.
Enhance the UI/UX for a polished appearance.
Continuously improve summarization accuracy and AI-generated content.
**Notes
-During development, I used the free resources of AssemblyAI and google gemini. 
 Warning
-Please be mindful of potential issues:

*Ensure that you do not exceed the token limit of the OpenAI or gemini ai API key.
 Be aware that the free services of AssemblyAI may have limitations.
 Contributing
//I welcome contributions from the community. Feel free to submit issues or pull requests to help me improve.

**Acknowledgments
  I extend our gratitude to AssemblyAI and OpenAI and google gemini for providing powerful AI services that make this project possible.


