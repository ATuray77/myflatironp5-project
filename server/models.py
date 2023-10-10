from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
#from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config import db, bcrypt

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ("-cars.user",)

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    _password_hash = db.Column(db.String, nullable=False)
    cars = db.relationship('Car', backref='user')

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    
    def __repr__(self):
        return f"\n<User id={self.id} first_name={self.first_name} last_name={self.last_name}email={self.email} user_name = {self.username} phone_number={self.phone}>"


class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    make_model = db.Column(db.String(100))
    color = db.Column(db.String(50))
    licence_plate = db.Column(db.String(20), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return f"\n<Car" \
            + f"id={self.id}, " \
            + f"make_model={self.make_model}, " \
            + f"color={self.color}, " \
            + f"license_plate={self.license_plate}, " \
            + ">"
    
#---a user table for authentication and login logic
# class User(db.Model, SerializerMixin):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50))
#     last_name = db.Column(db.String(50))
#     email = db.Column(db.String, unique = True, nullable = False)
#     username = db.Column(db.String(100), unique = True, nullable = False)
#     _password_hash = db.Column(db.String, nullable = False)

    

#---and of a user table for authentication and login logic


   
    
    