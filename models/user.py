#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
STRG = os.environ.get('HBNB_TYPE_STORAGE')

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if STRG == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable = False)
        password = Column(String(128), nullable = False)
        first_name = Column(String(128), nullable = False)
        last_name = Column(String(128), nullable = False)
