#!/usr/bin/python3


import json


class FileStorage:
    """Defines a file storage class"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initiates the class"""
        pass

    def all(self):
        """Returns the dictionary __objects
        
        Returns:
            dict: __objects
        """
        return self.__objects
    
    def new(self, obj):
        """Sets obj to the one with id
        
        Args:
            obj: object
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialize the __object"""
        json.dump(self.__objects, self.__file_path)

    def reload(self):
        """deserialize the json file"""
        pass
