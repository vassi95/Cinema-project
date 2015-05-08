import unittest
import sqlite3
from movies import Movie
from settings import DB_NAME

class TestMovie(unittest.TestCase):
    def test_movie(self):
        conn = sqlite3.connect(DB_NAME)
        mv = Movie.show_movies(conn)
        self.assertTrue(mv)


if __name__ == "__main__":
    unittest.main()
