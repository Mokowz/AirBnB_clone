#!/usr/bin/python3
"""Defines a base model"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines a base class"""

    def __init__(self, *args, **kwargs):
        """Instantiate the base class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"

            for (key, value) in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """String representation of base model"""
        str = '['
        str += str(self.__class__.__name__) + '] ('
        str += str(self.id) + ') ' + str(self.__dict__)
        return str

    def save(self):
        """updates the updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts __dict__ to a dictionary
        Returns:
            dict: dictionary
        """
        dict1 = self.__dict__.copy()
        dict1['__class__'] = self.__class__.__name__
        dict1['created_at'] = self.created_at.isoformat()
        dict1['updated_at'] = self.updated_at.isoformat()
        return dict1
