from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'super secret key'  # Necessary for session management

def get_db_connection():
    conn = sqlite3.connect('hw13.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM Students').fetchall()
    quizzes = conn.execute('SELECT * FROM Quizzes').fetchall()
    conn.close()
    return render_template('dashboard.html', students=students, quizzes=quizzes)

@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        conn = get_db_connection()
        conn.execute('INSERT INTO Students (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('add_student.html')

@app.route('/quiz/add', methods=['GET', 'POST'])
def add_quiz():
    if request.method == 'POST':
        subject = request.form['subject']
        number_of_questions = request.form['number_of_questions']
        date_given = request.form['date_given']
        conn = get_db_connection()
        conn.execute('INSERT INTO Quizzes (subject, number_of_questions, date_given) VALUES (?, ?, ?)', (subject, number_of_questions, date_given))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('add_quiz.html')

@app.route('/student/<int:id>')
def student_details(id):
    conn = get_db_connection()
    results = conn.execute('SELECT * FROM StudentResults WHERE student_id = ?', (id,)).fetchall()
    conn.close()
    return render_template('student_details.html', results=results, student_id=id)

@app.route('/results/add', methods=['GET', 'POST'])
def add_result():
    if request.method == 'POST':
        student_id = request.form['student_id']
        quiz_id = request.form['quiz_id']
        score = request.form['score']
        conn = get_db_connection()
        conn.execute('INSERT INTO StudentResults (student_id, quiz_id, score) VALUES (?, ?, ?)', (student_id, quiz_id, score))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM Students').fetchall()
    quizzes = conn.execute('SELECT * FROM Quizzes').fetchall()
    conn.close()
    return render_template('add_result.html', students=students, quizzes=quizzes)

if __name__ == '__main__':
    app.run(debug=True)
