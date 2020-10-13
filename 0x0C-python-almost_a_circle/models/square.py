#!/usr/bin/python3
""" Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square

    Args:
        Rectangle (class): Square inherits attributes
        and methods from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[{}] ({}) {}/{} - {}'.format(self.__class__.__name__,
                                             self.id, self.x,
                                             self.y, self.width)

    @property
    def size(self):
        """ Getter for size

        Returns:
            width: Rectangle's attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update values
        """
        attr = ['id', 'size', 'x', 'y']

        if args:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary representation of a
        Square
        """
        dict_rep = {'id': self.id, 'size': self.width,
                    'x': self.x, 'y': self.y}
        return dict_rep
