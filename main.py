"""
this is the "secret sauce" -- a single entry-point that resolves the
import dependencies.  If you're using blueprints, you can import your
blueprints here too.

then when you want to run your app, you point to main.py or `main.app`
"""
from app import app, db
import os
from models import *
from views import *

def create_tables():
    # Create table for each model if it does not exist.
    # Use the underlying peewee database object instead of the
    # flask-peewee database wrapper:
    db.create_tables([Person, Pet], safe=True)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))