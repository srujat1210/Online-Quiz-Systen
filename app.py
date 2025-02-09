from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# mysql connection
conn = mysql.connector.connect(
    host='localhost',
    user='quiz_user',
    password='sruja',
    database='quiz_db'
)
cursor = conn.cursor()

# home page 
@app.route('/')
def home():
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    return redirect('/login')

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            session['user'] = username
            return redirect('/')
    return render_template('login.html')

# quiz page
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    if request.method == 'POST':
        score = 0
        for q in questions:
            user_answer = request.form.get(str(q[0]))
            if user_answer == q[2]:
                score += 1
        cursor.execute("INSERT INTO scores (username, score) VALUES (%s, %s)", (session['user'], score))
        conn.commit()
        return redirect('/score')
    return render_template('quiz.html', questions=questions)

# score page
@app.route('/score')
def score():
    cursor.execute("SELECT * FROM scores WHERE username=%s", (session['user'],))
    scores = cursor.fetchall()
    return render_template('score.html', scores=scores)

# logout page
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
