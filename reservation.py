#!/usr/bin/env python3
from settings import HALL_SIZE

class Reservation:

    GET_RESERVED_PLACES='''
    SELECT COUNT(id) as reserved
    FROM Reservations
    WHERE projection_id=? '''


    @classmethod
    def free_spots(cls, conn, id):
        cursor = conn.cursor()
        cursor.execute(cls.GET_RESERVED_PLACES, (id, ))
        result = curr.fetchone()[0]
        total_spots = HALL_SIZE[0]*HALL_SIZE[1]
        return total_spots - result
