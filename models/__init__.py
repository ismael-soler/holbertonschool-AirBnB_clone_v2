#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

STRG = os.environ.get("HBNB_TYPE_STORAGE")

if STRG == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
