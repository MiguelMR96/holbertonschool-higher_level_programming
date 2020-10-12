#!/usr/bin/python3
""" Test for base models
"""


import unittest
import pep8
from models.rectangle import Rectangle


class testRectangle(unittest.TestCase):
    """ Test base class

    """
    def test_pep8(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/rectangle.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_Rectangle(self):
        self.assertTrue(True)

    def test_rectangle(self):
        self.assertTrue(True)

    def test_area(self):
        self.assertEqual(Rectangle())
