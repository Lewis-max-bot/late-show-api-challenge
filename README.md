# Late Show API

The **Late Show API** is a RESTful Flask backend for managing a fictional talk show. It handles Users, Guests, Episodes, and Appearances using a PostgreSQL database, JWT authentication, and Flask-Migrate for schema migrations.

---

## Features

- User registration and JWT-based login
- CRUD operations for Guests, Episodes, and Appearances
- Relationship mapping (e.g., Guests appearing in Episodes)
- Secure password hashing with Werkzeug
- PostgreSQL + Flask-Migrate + SQLAlchemy
- Modular MVC folder structure

---

## Tech Stack

- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Flask-Migrate (Alembic)
- **Auth**: Flask-JWT-Extended
- **Dev Tools**: Postman, .env, pipenv/venv

---

## Project Structure

late-show-api-challenge/
├── server/
│ ├── app.py
│ ├── config.py
│ ├── seed.py
│ ├── models/
│ │ ├── init.py
│ │ ├── user.py
│ │ ├── guest.py
│ │ ├── episode.py
│ │ └── appearance.py
│ └── controllers/
│ ├── auth_controller.py
│ ├── guest_controller.py
│ ├── episode_controller.py
│ └── appearance_controller.py
├── migrations/
├── .env
└── Pipfile / requirements.txt


---

## Setup Instructions

 1. Clone the Repository

```bash
git clone https://github.com/your-username/late-show-api.git
cd late-show-api

 2. Create a virtual Environment
python3 -m venv venv
source venv/bin/activate  # or source venv/bin/activate.fish

 3. Install Dependencies
pip install -r requirements.txt

 4. Set Environment Variables
FLASK_APP=server/app.py
FLASK_ENV=development
DATABASE_URL=postgresql://username:password@localhost:5432/late_show_db
JWT_SECRET_KEY=your_secret_key

 5. Run Migrations and Seed
export FLASK_APP=server/app.py
export PYTHONPATH=.
flask db upgrade
python3 server/seed.py

API Routes

🔹 Users
Method	
POST	
POST	

🔹 Guests
Method	
GET	
POST
DELETE	
🔹 Episodes
Method
GET	
POST	
DELETE	

🔹 Appearances
Method	
GET	
POST	
DELETE	




