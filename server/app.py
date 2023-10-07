#!/usr/bin/env python3

# Standard library imports
from sqlalchemy.exc import IntegrityError
# Remote library imports
from flask import request, session, make_response, jsonify
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Owner, Car, User


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
        email = data.get('email')
        username = data.get('username')
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


@app.route('/')
def index():
    return '<h1>Project Server</h1>'

# @app.route('/cars', methods=['GET'])
# def cars():
#     if request.method == 'GET':
#         cars = Car.query.all()

#         return make_response(
#             jsonify([cars.to_dict() for car in cars]),
#             200,
#         )

#     return make_response(
#         jsonify({"text": "Method Not Allowed"}),
#         405,
#     ) 
class Cars(Resource):
    def get(self):
        car_list = [c.to_dict() for c in Car.query.all()]
        response = make_response(
            car_list,
            200,
        )
        return response

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

        # production.ongoing = bool(request.form["ongoing"])
        # production.budget = int(request.form["budget"])

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

        response = make_response("", 204)

        return response


api.add_resource(CarByID, "/cars/<int:id>")

api.add_resource(Cars, "/cars")

api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

