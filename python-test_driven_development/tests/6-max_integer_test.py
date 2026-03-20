#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([10]), 10)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_all_same_numbers(self):
        """Test with all same numbers"""
        self.assertEqual(max_integer([4, 4, 4]), 4)

    def test_all_negative_same(self):
        """Test with all same negative numbers"""
        self.assertEqual(max_integer([-4, -4, -4]), -4)


if __name__ == '__main__':
    unittest.main()