#!/usr/bin/env python3

class Movie:

    GET_ALL_MOVIES = '''
    SELECT * FROM Movies
    ORDER BY rating '''

    GET_MOVIE_BY_ID = '''
    SELECT name, rating
    FROM Movies
    WHERE id=? '''

    @classmethod
    def show_movies(cls, conn):
        cursor = conn.cursor()
        return cursor.execute(cls.GET_ALL_MOVIES)

    @classmethod
    def get_movie(cls, conn, m_id):
        cursor = conn.cursor()
        cursor.execute(cls.GET_MOVIE_BY_ID, (m_id, ))

        return cursor.fetchall()[0]
