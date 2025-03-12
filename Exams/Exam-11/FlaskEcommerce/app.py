from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin

app=Flask(__name__)
app.config['SECRET_KEY']='key@123'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
db=SQLAlchemy(app)

login_manager=LoginManager(app)
login_manager.login_view='login'

from routes import *
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)