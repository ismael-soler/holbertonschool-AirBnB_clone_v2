#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os
STRG = os.environ.get('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """ Review class to store review information """
    if STRG == 'db':
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'))
        user_id = Column(String(60), ForeignKey('users.id'))
    else:
        place_id = ""
        user_id = ""
        text = ""
