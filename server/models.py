from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config import db, bcrypt

# Models go here!
class Owner(db.Model, SerializerMixin):
    __tablename__ = "owners"
    serialize_rules = ("-cars.owner",)

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Integer)
    last_name = db.Column(db.Integer)
    email = db.Column(db.String, unique = True, nullable = False)
    username = db.Column(db.String, unique = True)
    _password_hash = db.Column(db.String, nullable = False)

    cars = relationship("Car", backref="owner") # relationship


def __repr__(self):
        return f"\n<User id={self.id} first_name={self.first_namename} last_name={self.last_name}email={self.email} username={self.username}>"


class Car(db.Model, SerializerMixin):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key = True)
    make_model = db.Column(db.String, nullable = False)
    color = db.Column(db.String, nullable = False)
    license_plate = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, ForeignKey("owners.id"))


    def __repr__(self):
        return f"\n<Car" \
            + f"id={self.id}, " \
            + f"make_model={self.make_model}, " \
            + f"color={self.color}, " \
            + f"license_plate={self.license_plate}, " \
            + ">"