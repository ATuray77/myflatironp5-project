from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
#from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config import db, bcrypt

# Models go here!
# class Owner(db.Model, SerializerMixin):
#     __tablename__ = 'owners'
#     serialize_rules = ("-cars.owner",)

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.Integer)
#     last_name = db.Column(db.Integer)
#     email = db.Column(db.String, unique = True, nullable = False)
#     username = db.Column(db.String, unique = True)
#     phone = db.Column(db.Integer, unique = True)
#     _password_hash = db.Column(db.String, nullable = False)

#     cars = db.relationship("Car", backref="owner") # relationship


#     def __repr__(self):
#         return f"\n<User id={self.id} first_name={self.first_name} last_name={self.last_name}email={self.email} username={self.username} phone_number={self.phone}>"

#------
class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'
    serialize_rules = ("-cars.owner",)

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    _password_hash = db.Column(db.String(128))
    cars = db.relationship('Car', backref='owner')

    @property
    def username(self):
        return f'{self.first_name}_{self.last_name}'
    
    def __repr__(self):
        return f"\n<User id={self.id} first_name={self.first_name} last_name={self.last_name}email={self.email} user_name = f'{self.first_name}_{self.last_name}' phone_number={self.phone}>"
#-----

# class Car(db.Model, SerializerMixin):
#     __tablename__ = "cars"

#     id = db.Column(db.Integer, primary_key = True)
#     make_model = db.Column(db.String, nullable = False)
#     color = db.Column(db.String, nullable = False)
#     license_plate = db.Column(db.String, unique=True, nullable=False)
#     owner_id = db.Column(db.Integer, db.ForeignKey("owners.id"))



#-----
class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    make_model = db.Column(db.String(100))
    color = db.Column(db.String(50))
    licence_plate = db.Column(db.String(20), unique=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

#-----

    def __repr__(self):
        return f"\n<Car" \
            + f"id={self.id}, " \
            + f"make_model={self.make_model}, " \
            + f"color={self.color}, " \
            + f"license_plate={self.license_plate}, " \
            + ">"
    
#---a user table for authentication and login logic
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String, unique = True, nullable = False)
    username = db.Column(db.String(100), unique = True, nullable = False)
    _password_hash = db.Column(db.String, nullable = False)

    @property
    def username(self):
        return f'{self.first_name}_{self.last_name}'

#---and of a user table for authentication and login logic


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
        return f"\n<User id={self.id} first_name={self.first_name} last_name={self.last_name}email={self.email} user_name = f'{self.first_name}_{self.last_name}'>"