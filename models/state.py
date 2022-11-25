#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from os import getenv
from sqlalchemy.orm import relationship
import models


class State(BaseModel):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            list_cities = []
            list_obj = models.storage.all(city)
            for city in list_obj.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities