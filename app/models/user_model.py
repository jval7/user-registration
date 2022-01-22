from flask_sqlalchemy import SQLAlchemy

import app.config
from app.models.db import db, BaseModelMixin
from datetime import datetime

class UserModel(db.Model, BaseModelMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    email = db.Column(db.String(120))
    city = db.Column(db.String(120))

    def generate_log(self):
        with open(app.config.path, "a") as fo:
            fo.write("User created at: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " : " + '\n')
            fo.write(str({ "name": self.name,
                       "email": self.email,
                       "city": self.city}) + '\n')

