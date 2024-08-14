from flask import Flask
from werkzeug.security import check_password_hash
from flask_httpauth import HTTPBasicAuth
import logging
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600

auth = HTTPBasicAuth()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

logging.getLogger('app').info('Приложение запущено и ожидает новых подключений')


@auth.verify_password
# функция проверки пароля
def verify_pwd(username, password):
    for user in db.session.query(models.AdminUser).all():
        if username == user.name and check_password_hash(user.passw, password):
            return username


from . import (
    routes_admin, views, models
)
