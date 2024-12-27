from web_app import db
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

class User:
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_enc = db.Column(db.String(128))
    quiz_result = db.relationship('QuizScore', backref='user', lazy=True)

    def set_password(self, password):
        self.password_enc = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_enc, password)
    

class QuizScore:
    id= db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integar, db.ForeignKey('quiz.id'))
    user_id = db.Column(db.Integar, db.ForeignKey('user.id'))
    score = db.Column(db.Integar, nullable=False)
    score_date = db.Column(db.DateTime(timezone=True), default=datetime.now)
    
    
class Quiz:
    id= db.Column(db.Integer, primary_key=True)
    quiz_result = db.relationship('QuizScore', backref='quiz')
    questions = db.Column(db.List, nullable=False)
