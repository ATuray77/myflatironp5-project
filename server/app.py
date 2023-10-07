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
#---


@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

