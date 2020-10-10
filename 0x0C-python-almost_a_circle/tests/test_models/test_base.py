#!/usr/bin/python3
""" Test for base models
"""


import unittest
import pep8
from models.base import Base


class testBase(unittest.TestCase):
    """ Test base class

    """
    def test_pep8(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["../models/base.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_Base(self):
        self.assertTrue(True)

    def test_base(self):
        self.assertTrue(True)

    def test_id_1(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
