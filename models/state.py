#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv
from models.city import City

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """
    State class
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """
            Returns the list of City instances with state_id
            equals to the current State.id
            """
            from models import storage
            all_cities = storage.all(City)
            my_city = []
            city_obj = all_cities.values()
            for obj in city_obj:
                if obj.state_id == self.id:
                    my_city.append(obj)
            return my_city
