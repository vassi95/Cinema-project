#!/usr/bin/env python3
from projections import Projection
import sqlite3
import unittest

class TestProjection(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect('cinema.db')

    def test_get_projection(self):
        p = Projection.get_projection(self.db,1,'2014-04-02');
        self.assertTrue(p)



if __name__ == "__main__":
    unittest.main()
