#!/usr/bin/python3
""" Base class
"""
import os
import json


class Base:
    """ Base class for other subclasses
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the json string representation of
        list dictionaries

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the json string representation of list_objs
        to a file

        Args:
            list_objs (list of instances): list of instances who inherits
            of Base
        """
        new_l = []

        with open(cls.__name__ + '.json', 'w') as fd:
            if not list_objs:
                return fd.write(cls.to_json_string(new_l))
            for i in list_objs:
                dic = cls.to_dictionary(i)
                new_l.append(dic)
            return fd.write(cls.to_json_string(new_l))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation

        Args:
            json_string (json): string representing a list of dictionaries
        """
        if not json_string or len(json_string) == 0:
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            tmp = cls(1, 1)
        elif cls.__name__ == 'Square':
            tmp = cls(1)

        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances
        """
        new_l = []

        if os.path.isfile(cls.__name__ + '.json'):
            with open(cls.__name__ + '.json', 'r') as fd:
                string = fd.read()
                list_json = cls.from_json_string(string)
                for x in list_json:
                    new_l.append(cls.create(**x))
        return new_l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV

        Args:
            list_objs (obj): list of objects
        """
        new_l = []

        with open(cls.__name__ + '.csv', 'w') as fd:
            if list_objs:
                new_l = [i.to_dictionary() for i in list_objs]
            fd.write(cls.to_json_string(new_l))

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes in CSV
        """
        new_l = []

        if os.path.isfile(cls.__name__ + '.csv'):
            with open(cls.__name__ + '.csv', 'r') as fd:
                string = fd.read()
                list_csv = cls.from_json_string(string)
                for i in list_csv:
                    new_l.append(cls.create(**i))
        return new_l
