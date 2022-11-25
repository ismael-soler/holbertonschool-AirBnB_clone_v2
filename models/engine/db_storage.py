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

    __engine = None
    __session = None

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

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
        """query database session"""

        obj_dict = dict()
        if cls is None:
            for currentClass in DBStorage.classes.values():
                for obj in self.__session.query(currentClass).all():
                    obj_dict[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for obj in self.__session.query(DBStorage.classes[cls]).all():
                obj_dict[obj.__class__.__name__ + '.' + obj.id] = obj
        return obj_dict

    def reload(self):
        """ Create all tables in th current DB and the current session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def new(self, obj):
        """ Adding an object to the current DB """
        self.__session.add(obj)
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an instance from the current DB """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def delete(self, obj=None):
        """ Deletes an instance from the current DB """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def close(self):
        """ Close method to call remove() method """
        self.__session.close()
