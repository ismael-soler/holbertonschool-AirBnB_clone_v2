#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os


if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    classes = DBStorage.classes
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    classes = FileStorage.classes
    storage = FileStorage()
storage.reload()
