#!/usr/bin/python3
"""
Unit tests for base class
"""
from unittest import TestCase

from models.base import Base


class TestBase(TestCase):
    """Tests the Base class"""
    def test_id(self):
        """Tests the behavior of id as we create more and more base objects"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)
