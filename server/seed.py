#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import random 
# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Car, Owner

if __name__ == '__main__':
    fake = Faker()


    with app.app_context():
        print("Starting seed...")
        #Seed code goes here!
        Owner.query.delete()
        Car.query.delete()

        print("Creating Owner...")
        owner_list = []
        for _ in range(10):

            first_name=fake.first_name()
            last_name=fake.last_name()
            username = f"{first_name}_{last_name}"
            phone = fake.phone_number()


            owner = Owner(first_name=first_name, last_name=last_name, username = username, phone=phone, email = fake.ascii_email())
            owner_list.append(owner)
        db.session.add(owner_list)
        db.session.commit()
        #owner_list.append(owner)



        print("Creating Car...")
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
            "Teals_Model 3"
            ]
        colors = ["white", "red", "green", "blue", "yellow", "purple", "brown", "pink", "grey", "black"]
        # print(makes_models)
        # print(colors)
        cars_list = []
        for i in range(10):
            car = Car(
                make_model = random.choice(makes_models),
                color = random.choice(colors),
                license_plate = fake.license_plate()
            )

            owner = random.choice(owner_list)
            owner.cars.append(car)
            cars_list.append(car)
            print(cars_list)

        db.session.add_all(cars_list)
        db.session.commit()