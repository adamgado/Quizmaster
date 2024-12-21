from web_app import app

@app.route('/')
def homepage():
    return 'Homepage'
    
@app.route('/quizzes')
def quiz_list():
    return 'list of quizzes'

@app.route('/quiz')
def current_quiz():
    return 'quiz'