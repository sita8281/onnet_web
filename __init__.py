from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
import logging
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crm.db')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

logging.getLogger('app').info('Приложение запущено и ожидает новых подключений')

users = {
    "ivan": generate_password_hash("Miron4ik@"),
    "artem": generate_password_hash("123kl123kl"),
    "varya": generate_password_hash("12041204"),
}


@auth.verify_password
# функция проверки пароля
def verify_pwd(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


from . import (
    views, views_cabinet, views_crm, models
)
