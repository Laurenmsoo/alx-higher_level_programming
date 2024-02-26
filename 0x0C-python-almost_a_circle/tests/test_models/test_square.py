#!/usr/bin/python3
""" Module for testing square class """
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """ Test cases for square class """

    def test_constructor(self):
        """ Test the constructor """

        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Square(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Square(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_setters(self):
        """ Test the setters """

        r = Square(10, 2)

        r.width = 5
        self.assertEqual(r.width, 5)

        r.height = 8
        self.assertEqual(r.height, 8)

        r.x = 3
        self.assertEqual(r.x, 3)

        r.y = 4
        self.assertEqual(r.y, 4)

    def test_invalid_setters(self):
        """ Test invalid values for setters """

        r = Square(10, 2)

        with self.assertRaises(TypeError):
            r.width = "invalid"

        with self.assertRaises(ValueError):
            r.width = 0

        with self.assertRaises(TypeError):
            r.height = "invalid"

        with self.assertRaises(ValueError):
            r.height = 0

        with self.assertRaises(TypeError):
            r.x = "invalid"

        with self.assertRaises(ValueError):
            r.x = -1

        with self.assertRaises(TypeError):
            r.y = "invalid"

        with self.assertRaises(ValueError):
            r.y = -1

if __name__ == "__main__":
    unittest.main()

