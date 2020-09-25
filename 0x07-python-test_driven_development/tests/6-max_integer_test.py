#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import pep8
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unit test
    """

    def test_pep8(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["6-max_integer.py"])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")    
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    def test_not_list(self):
        self.assertEqual(max_integer("Miguel"), 'u')
