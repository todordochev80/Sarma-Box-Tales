1. Project Overview 📖
Sarma Box Tales – платформа за абсурдни истории. Спомени, че използваш Django и DRF.

2. Features 
User Management: Extended User Model, Profiles, Roles.

Stories: Full CRUD functionality, categories, and search.

API: RESTful endpoints for stories.

Async Tasks: Celery & Redis for welcome emails.

Security: CSRF protection, .env configuration, login requirements.

3. Tech Stack 🛠️
Framework: Django, Django REST Framework

Database: PostgreSQL

Task Queue: Celery & Redis

Styling: Bootstrap / Custom CSS

Environment: Python-dotenv

4. Local Setup Instructions 🚀

Clone the repo: git clone ...

Virtual Env: python -m venv .venv и source .venv/bin/activate

Install requirements: pip install -r requirements.txt

Database: Настройте PostgreSQL и създайте база данни.

Migrations: python manage.py migrate

Admin: python manage.py createsuperuser

Run: python manage.py runserver

5. Environment Variables (.env) 🔐
примерна структура (SAMPLE), без да разкриваш истински пароли:
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=sarma_box_tales_db
DB_USER=postgres
DB_PASS=your_pass
DB_HOST=127.0.0.1
DB_PORT=5432

6. Testing 🧪
15 unit tests, обхващащи модели, форми и изгледи. Пускат се с: python manage.py test.