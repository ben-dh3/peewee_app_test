from peewee import *
from flask import Flask

app = Flask(__name__)
# name of database
db = SqliteDatabase('peewee_app.db')
