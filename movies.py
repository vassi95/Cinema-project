#!/usr/bin/env python3

class Movie:

    GET_ALL_MOVIES = '''
    SELECT * FROM Movies
    ORDER BY rating '''

    @classmethod
    def show_movies(cls, conn):
        cursor = conn.cursor()
        return cursor.execute(cls.GET_ALL_MOVIES)
