#!/usr/bin/python3
"""class define databasestorage"""

from os import environ
from sqlalchemy import create_engine, MetaData
from models.base_model import Base, BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """DB Storage"""

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    __engine = None
    __session = None

    def __init__(self):
        """engine must be linked to the MySQL database and user created"""

        user = environ.get("HBNB_MYSQL_USER")
        pwd = environ.get("HBNB_MYSQL_PWD")
        host = environ.get("HBNB_MYSQL_HOST")
        db = environ.get("HBNB_MYSQL_DB")
        env = environ.get("HBNB_MYSQL_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, pwd, host, db), pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        It returns a dictionary of all objects in the database.
        """
        classes = DBStorage.classes
        obj_dict = {}

        for currentClass in classes:
            if classes[currentClass] == cls or cls is None:
                for obj in self.__session.query(classes[currentClass]).all():
                    obj_dict[type(obj).__name__ + '.' + obj.id] = obj
        return obj_dict

    def new(self, obj):
        """"add current obj"""
        self.__session.add(obj)

    def save(self):
        """""save all changes datbase"""
        self.__session.commit()

    def delete(self, obj=None):
        """""delete from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in th current DB and the current session """
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(new_session)
        self.__session = Session

    def close(self):
        """close"""
        self.__session.close()
