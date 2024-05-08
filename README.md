# IS211_Assignment12
IS211_Assignment12
Flask Web Application (2/2)
This Flask web application is designed to manage a classroom setting, where teachers can add and view students, quizzes, and quiz results. The application uses SQLite for its database backend.

Features
User authentication (simple login with hard-coded credentials).
Ability to add students to the class.
Ability to add quizzes.
Ability to view all students and quizzes.
Ability to add quiz results for each student.
Ability to view quiz results for each student.

Installation
To get this project up and running, you'll need Python and Flask installed on your system.

Clone the repository:
git clone https://github.com/yourusername/IS211_Assignment13.git
cd IS211_Assignment13

Install the required packages:
pip install -r requirements.txt

Setting Up the Database:
Run the following command to create your SQLite database using the schema provided:
sqlite3 hw13.db < schema.sql

This command sets up the necessary database tables and can be used to load initial data if you modify the schema file to include insert statements.

Running the Application
To run the application, execute the following command from the root of the project directory:
python app.py

This will start the Flask server, typically on http://127.0.0.1:5000, where you can access the application via your web browser.

Usage
Visit http://127.0.0.1:5000/login to access the application.
Login with the username admin and password password.
Follow the navigational links to view students, quizzes, or add new data to the system.





