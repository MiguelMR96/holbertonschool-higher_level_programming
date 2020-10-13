#!/usr/bin/python3
""" Base class
"""


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
                return fd.write(new_l)
            for i in list_objs:
                dic = cls.to_dictionary(i)
                new_l.append(dic)
            return fd.write(cls.to_json_string(new_l))
