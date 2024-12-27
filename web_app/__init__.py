from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config["SECRET_KEY"] = "w648v87qny487q"
app.config["SQLALCHEMY_DATABASE_URL"] = 'sqlite:///users_informations.db'
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

from web_app import views
from web_app import models

app.config.from_object('configuration')
