from data.users import User
from flask import Flask
from data import db_session
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

