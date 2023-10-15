#!/usr/bin/env python3
# serializes instances to a JSON file and deserializes JSON file to instances

import json
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """Serialize and deserialize instances to and from a JSON file.

        Attributes:
            __file_path (str): The path to the JSON file.
            __objects (dict): A dictionary to store serialized objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Set an object in __objects with a key of <obj class name>.id.
            Args:
                obj (object): The object to be stored.
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        value = obj
        self.__objects[key] = value

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        classes = {
                'BaseModel': BaseModel,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review,
        }
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                from_json = json.load(f)
                if from_json is None:  # empty file
                    pass  # do nothing
                else:
                    for key, value in from_json.items():
                        class_name = value['__class__']
                        if class_name in classes:
                            instance_class = classes[class_name]
                            instance = instance_class(**value)
                            self.__objects[key] = instance
        except FileNotFoundError:
            pass
