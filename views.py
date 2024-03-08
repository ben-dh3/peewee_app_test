"""
views imports app, auth, and models, but none of these import views
"""
from flask import Flask
from datetime import date
from app import app
from models import Person, Pet

@app.route("/")
def hello_world():
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
    uncle_bob.save() # bob is now stored in the database
    # Returns: no. of rows modified i.e. 1
    grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
    herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
    # change a value
    grandma.name = 'Grandma L.'
    grandma.save()  # Update grandma's name in the database.
    # Returns: 1

    Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    Pet.create(owner=herb, name='Fido', animal_type='dog')
    Pet.create(owner=herb, name='Mittens', animal_type='cat')
    Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

    pets = []
    for pet in Pet.select().where(Pet.owner == herb):
        pets.append(pet.name)
    return f"{pets}"