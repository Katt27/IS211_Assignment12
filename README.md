# IS211_Assignment12 - Flask Web Application Part 2

This Flask web application manages a classroom setting where teachers can add and view students, quizzes, and quiz results. The application uses SQLite for its database backend.

## Features
- User authentication (simple login with hardcoded credentials).
- Ability to add and view students and quizzes.
- Ability to add and view quiz results.

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/IS211_Assignment13.git
cd IS211_Assignment13
pip install -r requirements.txt

Setting Up the Database
Create the database using the provided schema:
sqlite3 hw13.db < schema.sql

Running the Application
Run the app with:
python app.py

Access the web application at http://127.0.0.1:5000.
