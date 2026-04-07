Sarma Box Tales 📖
Django Advanced Project @ SoftUni

Sarma Box Tales is a unique storytelling platform built with Django, designed for sharing and exploring "absurd and funny" stories. This project demonstrates advanced backend architecture, asynchronous task processing, and RESTful API integration.

✨ Core Features
Custom User Management: Extended Storyteller model with profiles, custom avatars, and community ranks.

Story Engine: Full CRUD for stories, categorized by "Sarma Boxes" with tagging support.

RESTful API: Fully documented API endpoints for stories using Django REST Framework.

Asynchronous Tasks: Automated welcome emails triggered by registration using Celery and Redis.

Advanced Search: Filter-ready search system by content, category, author, and tags.

Security: Robust protection with environment variables, CSRF tokens, and role-based permissions (Moderators/Authors).

🛠️ Technical Stack
Framework: Django 5.x / Django REST Framework

Database: PostgreSQL

Task Queue: Celery & Redis

Testing: Django TestCase (15 units covering Models, Forms, and Views)

Styling: Bootstrap 5 & Custom CSS

🔧 Local Setup Instructions
Clone the repository:

Bash
git clone <https://github.com/todordochev80/Sarma-Box-Tales>
cd sarma_box_tales
Setup Virtual Environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
Environment Configuration:
Create a .env file in the root directory based on the .env.sample provided below.

Migrations:

Bash
python manage.py migrate
Start Celery Worker (Required for emails):

Bash
celery -A sarma_box_tales worker -l info
Run Server:

Bash
python manage.py runserver
🔐 Environment Variables (.env.sample)
Фрагмент от код
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=sarma_box_tales_db
DB_USER=postgres
DB_PASS=your_db_password
DB_HOST=127.0.0.1
DB_PORT=5432
CELERY_BROKER_URL=redis://127.0.0.1:6379/0
🧪 Testing
The project includes 15 automated tests. Run them using:

Bash
python manage.py test
🌐 API Documentation
List Stories: GET /stories/api/

Story Detail: GET /stories/api/<id>/

Create Story: POST /stories/api/ (Requires Authentication)

🔗 **[Live Demo](http://16.171.196.93)**