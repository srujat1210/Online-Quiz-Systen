**Online-Quiz-Systen 🎯**

A simple Flask + MySQL based Online Quiz System where users can log in, take quizzes, and track their scores.

**🚀 Tech Stack**

Frontend: HTML, Bootstrap, Jinja2

Backend: Python (Flask)

Database: MySQL

**🛠️ Installation Guide**

1️⃣ Clone the Repository

2️⃣ Install Dependencies.
Make sure you have Python 3.10+ installed, then install required libraries:
pip install flask mysql-connector-python

3️⃣ Set Up MySQL Database
Open MySQL and create a database:

CREATE DATABASE quiz_db;
USE quiz_db;
> Run the provided SQL script to create tables:

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    correct_answer CHAR(1) NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL
);


CREATE TABLE scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    score INT NOT NULL,
    quiz_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
> Insert sample questions

4️⃣ Configure Database Connection
In app.py, update your MySQL connection details.
