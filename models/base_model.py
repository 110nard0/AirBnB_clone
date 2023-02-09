#!/usr/bin/python3
"""Base_Model module contains a base class for all class objects
"""
from models import storage
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Class constructor for new base instance object

        Attributes:
            id (str): universal unique identifier of instance
            created_at (obj): datetime object current date and time of creation
            created_at (obj): datetime object showing current date and time
        """
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.fromisoformat(str(v)))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Returns the official string representation of instance object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns:
            dictionary (dict): all keys/values of __dict__ of the instance:
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            dictionary[key] = value
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
