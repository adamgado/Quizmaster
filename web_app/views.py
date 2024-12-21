from web_app import app
from flask import render_template

@app.route('/')
def homepage():
    return render_template('homepage.html')
    
@app.route('/quizzes')
def quiz_list():
    return 'list of quizzes'

@app.route('/quiz')
def current_quiz():
    return 'quiz'
