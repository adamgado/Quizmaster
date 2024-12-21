from web_app import app
from flask import render_template, request

@app.route('/')
def homepage():
    return render_template('main.html')
    
@app.route('/register', methods=['Post'])
def register_page():
    username = request.form['name']
    email_address = request.form['email-address']
    password = request.form['password']
    return username + " registered successfully"

@app.route('/quizzes')
def quiz_list():
    return 'list of quizzes'

@app.route('/quiz')
def current_quiz():
    return 'quiz'
