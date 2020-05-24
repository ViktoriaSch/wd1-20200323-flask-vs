import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "postgres://cseitffdkftjax:3cf4cd23efd56eab42a3245d8490817261b3bedff216910dc638e79f16642f43@ec2-54-246-90-10.eu-west-1.compute.amazonaws.com:5432/d3tsrlcgkeiqj0"))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    secret_number = db.Column(db.Integer, nullable=True)

class SecretNumberStore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cookie_identifier = db.Column(db.String, unique=True, nullable=False)
    secret_number = db.Column(db.Integer, nullable=False)



