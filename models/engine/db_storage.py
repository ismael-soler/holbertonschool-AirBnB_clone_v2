#!/usr/bin/python3
"""Database Storage"""


from models.user import User
from models.base_model import BaseModel
from models.base_model import Base
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

model = {"User": User, "State": State,
         "City": City, "Amenity": Amenity,
         "Place": Place, "Review": Review}


class DBStorage():
    """Database"""
    __engine = None
    __session = None

    def __init__(self):
        """inisialization"""
        self.__engine = create_engine(('mysql+mysqldb://{}:{}@{}/{}')
                                        .format(getenv('HBNB_MYSQL_USER'),
                                                getenv('HBNB_MYSQL_PWD'),
                                                getenv('HBNB_MYSQL_HOST'),
                                                getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.meta.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """all func"""
        objs = {}
        for cclass in model:
            if model[cclass] == cls or cls is None:
                for key in self.__session.query(model[cclass]).all():
                    objs[type(key).__name__+'.'+key.id] = key
        return objs

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj == None:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        ssession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ssession)
        self.__session = Session

    def close(self):
        """close"""
        self.__session.close()
