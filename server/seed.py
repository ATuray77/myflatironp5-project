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
        # owner_list = []
        # for n in range(10):

        #     first_name=fake.first_name()
        #     last_name=fake.last_name()
        #     email = fake.ascii_email()
        #     username = f"{first_name}_{last_name}"
        #     phone = fake.phone_number()


        #     owner = Owner(
        #         first_name=first_name, 
        #         last_name=last_name, 
        #         email = email, 
        #         username = username, 
        #         phone=phone, 
        #     )
        #     owner.password_hash = owner
            
        #     owner_list.append(owner)
        # db.session.add_all(owner_list)
        # db.session.commit()
        # #owner_list.append(owner)
        # print(owner_list)



        # print("Creating Car...")
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
        # colors = ["white", "red", "green", "blue", "yellow", "purple", "brown", "pink", "grey", "black"]
        # # print(makes_models)
        # # print(colors)
        # cars_list = []
        # for i in range(10):
        #     car = Car(
        #         make_model = random.choice(makes_models),
        #         color = random.choice(colors),
        #         license_plate = fake.license_plate()
        #     )

        #     owner = random.choice(owner_list)
        #     owner.cars.append(car)
        #     cars_list.append(car)
        #     print(cars_list)

        # db.session.add_all(cars_list)
        # db.session.commit()

#----

        db.create_all()

        # generate 10 owners
        for _ in range(10):
            
            owner = Owner(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                username = fake.user_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                #_password_hash=fake.sha256()
            )
            db.session.add(owner)

        # commit the owners to the database so they get primary keys
        db.session.commit()

        # generate 30 cars
        for _ in range(30):
            car = Car(
                #make_model=fake.company(),
                make_model = random.choice(makes_models),
                color=fake.safe_color_name(),
                licence_plate=fake.license_plate(),
                owner_id=random.choice(Owner.query.all()).id
            )
            db.session.add(car)

        # commit the cars to the database
        db.session.commit()

#----
