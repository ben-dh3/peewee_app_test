"""
models imports app, but app does not import models so we haven't created
any loops.
"""
from peewee import *

from app import db

# model class -> database table
class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "peewee_app.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "peewee_app.db" database

db.connect()