#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import random 
# Remote library imports
from faker import Faker

# Local imports

from app import app
from models import db, Car, User

if __name__ == '__main__':
    fake = Faker()


    with app.app_context():
        print("Starting seed...")
        #Seed code goes here!
        User.query.delete()
        Car.query.delete()

        print("Creating Users...")
       
        makes_models = [
            "Toyota_Camry", 
            "Ford_Mustang", 
            "Cheverolet_Camaro", 
            "Honda_Pilot", 
            "Audi_A4", 
            "Hyundai_Elantra", 
            "Kia_Golf", 
            "Lexus_ES", 
            "BMW_X6", 
            "Teals_Model 3",
            "Mercedes_C",
            "BMW_X5",
            "Tesla_ModelC",
            "Dodge_Charger"
            "Dodge_Challenger"
            ]
      

#----

        db.create_all()

        # generate 10 owners
        for _ in range(10):
            
            user = User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                username = fake.user_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                _password_hash=fake.sha256()
            )
            db.session.add(user)

        # commit the owners to the database so they get primary keys
        db.session.commit()

        # generate 30 cars
        for _ in range(30):
            car = Car(
                make_model = random.choice(makes_models),
                color=fake.safe_color_name(),
                licence_plate=fake.license_plate(),
                user_id=random.choice(User.query.all()).id
            )
            db.session.add(car)

        # commit the cars to the database
        db.session.commit()

#----
