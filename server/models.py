from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

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



    def __repr__(self):
        return f"\n<Owner" \
            + f"id={self.id}, " \
            + f"first_name={self.first_name}, " \
            + f"last_name={self.last_name}, " \
            + f"username={self.username}, " \
            + f"phone={self.phone}, " \
            + f"email={self.email}, " \
            + ">"


class Car(db.Model, SerializerMixin):
    __tablename__ = "cars"

    id = Column(Integer, primary_key = True)
    make_model = Column(String, nullable = False)
    color = Column(String, nullable = False)
    license_plate = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("owners.id"))


    def __repr__(self):
        return f"\n<Car" \
            + f"id={self.id}, " \
            + f"make_model={self.make_model}, " \
            + f"color={self.color}, " \
            + f"license_plate={self.license_plate}, " \
            + ">"