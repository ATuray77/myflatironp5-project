from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class Owner(db.Model, SerializerMixin):
    __tablename__ = "owners"
    serialize_rules = ("-cars.owner",)

    id = Column(Integer, primary_key = True)
    first_name = Column(String, nullable= False)
    last_name = Column(String, nullable= False)
    username = Column(String, unique=True, nullable=False )
    phone= Column(String, nullable = False)
    email= Column(String, unique=True)

    cars = relationship("Car", backref="owner") # relationship