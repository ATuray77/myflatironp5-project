#!/usr/bin/env python3

# Standard library imports
from sqlalchemy.exc import IntegrityError
# Remote library imports
from flask import request, session, make_response, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Car


# Views go here!
#---
class ClearSession(Resource):

    def delete(self):
    
        session['page_views'] = None
        session['user_id'] = None

        return {}, 204
    
class Signup(Resource):
    def post(self):
        data = request.get_json()

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        email = data.get('email')
        phone = data.get('phone')
        
        password = data.get('password')
        

        if not username or not password:
            return ({'message': 'Missing username or password'}), 422

        existing_user = User.query.filter(User.username==username).first()
        if existing_user:
            return ({'message': 'User already exists'}), 422

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            phone=phone
        )
        user.password_hash = password

        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id

        return user.to_dict(), 201
    
class CheckSession(Resource):

    def get(self):

        if session.get('user_id'):
            
            user = User.query.filter(User.id == session['user_id']).first()
            
            return user.to_dict(), 200

        return {}, 204
    

class Login(Resource):

    def post(self):
        
        username = request.get_json()['username']
        password = request.get_json()['password']

        user = User.query.filter(User.username == username).first()

        if user.authenticate(password):

            session['user_id'] = user.id
            return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401
    
class Logout(Resource):
    def delete(self):
    
        session['user_id'] = None
        
        return {}, 204
#---


# @app.route('/')
# def index():
#     return '<h1>WELCOME TO METRO PARKNG GARAGE</h1>'


class Home(Resource):

    def get(self):

        response_dict = {
            "message": "The safest parking garage in downtown",
        }

        response = make_response(
            response_dict,
            200
        )

        return response



class Cars(Resource):
    def get(self):
        car_list = [c.to_dict() for c in Car.query.all()]
        response = make_response(
            car_list,
            200,
        )
        return response


    def post(self):
        json = request.get_json()
        if not session.get('user_id'):
            return ({"error":"unauthorized"}, 401)
        else:
            try:
                new_car = Car(
                    make_model = json['make_model'],
                    color = json['color'],
                    licence_plate = json['licence_plate'],
                    user_id = session['user_id'],
                    )
            
                db.session.add(new_car)
                db.session.commit()
                
                response_dict = new_car.to_dict()
                response = make_response(
                    response_dict, 
                    201,
                )
                return response

            except IntegrityError:
                db.session.rollback()
                return {"error":"unprocessable entity"}, 422
#---End post

class CarByID(Resource):
    def get(self, id):
        car = Car.query.filter_by(id=id).first()
        if not car:
            return {"error": "Production not found"}, 404
        car_dict = car.to_dict()
        response = make_response(car_dict, 200)
        return response

    def patch(self, id):
        car = Car.query.filter_by(id=id).first()
        if not car:
            return {"error": "Production not found"}, 404

        for attr in request.form:
            setattr(car, attr, request.form[attr])


        db.session.add(car)
        db.session.commit()

        car_dict = car.to_dict()

        response = make_response(car_dict, 200)
        return response

    def delete(self, id):
        car = Car.query.filter_by(id=id).first()
        if not car:
            return {"error": "Production not found"}, 404
        db.session.delete(car)
        db.session.commit()

        response_dict = {"message": "record successfully deleted"}
        response = make_response(
            response_dict,
             200)

        return response


#---all cars belonging to a user
class AllmyCars(Resource):
    def get(self, id):

        user_id = session.get('user_id')
        if user_id is None:
            return {"error": "No user logged in"}
        
        cars = Car.query.filter_by(id=user.id).all()
        car_data = [
            {
                "make_model": car.make_model,
                "color": car.color,
                "license_plate": car.license_plate
            } for car in cars
        ]

        cars_dict = car_data.to_dict()
        response = make_response(cars_dict, 200)
        
        return response

api.add_resource(AllmyCars, '/allmyCars/<int:id>')

#---end all cars belonging to a user

#---start of all users route
class Users(Resource):
    def get(self):
        user_list = [u.to_dict() for u in user.query.all()]
        response = make_response(
            user_list,
            200,
        )
        return response
api.add_resource(Users, '/users')
#---end of all users route

#---start users resources byid, patch and delete
class UserByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return {"error": "user not found"}, 404
        user_dict = user.to_dict()
        response = make_response(user_dict, 200)
        return response

    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return {"error": "User not found"}, 404

        for attr in request.form:
            setattr(user, attr, request.form[attr])


        db.session.add(user)
        db.session.commit()

        user_dict = user.to_dict()

        response = make_response(user_dict, 200)
        return response

    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            return {"error": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()

        response = make_response("", 204)

        return response
api.add_resource(UserByID, '/users/<int:id>')
#---end users resources byid, patch and delete



api.add_resource(CarByID, '/cars/<int:id>')
api.add_resource(Cars, '/cars')
api.add_resource(Home, '/')


api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

