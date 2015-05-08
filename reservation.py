#!/usr/bin/env python3
from settings import HALL_SIZE

class Reservation:

    GET_RESERVED_PLACES='''
    SELECT COUNT(id) as reserved
    FROM Reservations
    WHERE projection_id=? '''

    MAKE_RESERVATION='''
    INSERT INTO Reservations(id, username, projection_id, row, col)
    VALUES(?, ?, ?, ?, ?) '''

    @classmethod
    def get_last_id(cls, conn):
        curr = conn.cursor()
        curr.execute('''SELECT MAX(id) FROM Reservations''')
        return curr.fetchone()[0]

    @classmethod
    def free_spots(cls, conn, id):
        cursor = conn.cursor()
        cursor.execute(cls.GET_RESERVED_PLACES, (id, ))
        result = cursor.fetchone()[0]
        total_spots = HALL_SIZE[0]*HALL_SIZE[1]
        return total_spots - result

    @classmethod
    def reserve(cls, conn, tpl):
        user, proj_id, row, col = tpl
        id = cls.get_last_id(conn) + 1
        crsr=conn.cursor()
        crsr.execute(cls.MAKE_RESERVATION, (id, user, proj_id, row, col))
        conn.commit()