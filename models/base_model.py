#!/usr/bin/python3
"""defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, DateTime
import os

STRG = os.environ.get('HBNB_TYPE_STORAGE')


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    if STRG == 'db':
        id = Column(String(60), primary_key=True)
        created_at = Column(
            DateTime,
            nullable=False,
            default=datetime.utcnow()
        )
        updated_at = Column(
            DateTime,
            nullable=False,
            default=datetime.utcnow()
        )

    def __init__(self, *args, **kwargs):
        """instantiantities a new model"""
        date = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, date))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            dictionary.pop('_sa_instance_state', None)
        return dictionary


    def delete(self):
        """ Deletes an instance """
        from models import storage
        storage.delete(self)
