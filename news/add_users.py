from data.users import User
from flask import Flask
from data import db_session
from data.jobs import

db_session.global_init("db/blogs.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

user = User()
user.name = "Admin"
user.about = "adimin site"
user.email = "email@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

