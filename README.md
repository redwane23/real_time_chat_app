1/ Real Time Chat App
This Django project enables real-time communication between users using Django Channels and WebSockets.
It supports both private messaging and group chats, making it easy to interact with multiple users simultaneously.

2/ Feature
- User Authentication: Secure login and logout functionality.
- Profile Management: Users can manage and update their profiles.
- Private and Group Chats: Ability to create private chats as well as public group conversations.
- Search Filters: Easily search for rooms or users.
- Paginated Message Loading: Efficient loading of chat messages for a smooth user experience.
- Optimised APIs: Optimized APIs: APIs optimized for maximum efficiency and reduced database access, monitored with Django Silk.
- 
3/ clonigng proccess
- git clone https://github.com/redwane23/real_time_chat_app.git
- python -m venv venv
- source venv/bin/activate  # macOS/Linux or use venv\Scripts\activate on Windows
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver #for wsgi mode and uvicorn Message.asgi:application --host 0.0.0.0 --port 8000
