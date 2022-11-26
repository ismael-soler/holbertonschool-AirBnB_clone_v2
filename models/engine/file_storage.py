#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            objs_result = {}
            # Checks each object inside __objects and compare if a key
            # == to our cls class filter:
            for key, value in FileStorage.__objects.items():
                if key.split(".")[0] == cls.__name__:
                    objs_result[key] = FileStorage.__objects[key]
            # In objs_result we save all the filtered results:
            return objs_result

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from the storage"""
        if obj is None:
            return

        # In JSON file we save all the new objects like:
        # Place.213bhj231af3 = name of the object "." object.id:
        key = f"{type(obj).__name__}.{obj.id}"

        # If this key exists in __object, we have an object to be deleted:
        if key in self.all():
            objects_dict = self.all()
            objects_dict.pop(key)
            self.save()