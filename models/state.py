#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship("City", backref="state", cascade="all, \
                              delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """init state"""
        super().__init__(*args, **kwargs)

    if (getenv("HBNB_TYPE_STORAGE") != "db"):
        @property
        def cities(self):
            """cities"""
            from models import storage
            stacit = []
            for stat in storage.all(City).values():
                if self.id == city.state_id:
                    stacit.append(storage.all(City)[stat])
            return stacit