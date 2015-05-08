#!/usr/bin/env python3
from settings import HALL_SIZE


class Reservation:

    GET_RESERVED_PLACES = '''
    SELECT COUNT(id) as reserved
    FROM Reservations
    WHERE projection_id=? '''

    MAKE_RESERVATION = '''
    INSERT INTO Reservations(id, username, projection_id, row, col)
    VALUES(?, ?, ?, ?, ?) '''

    GET_RESERVED_SEATS = '''
    SELECT COUNT(id) FROM Reservations WHERE row=? AND col=?'''

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
        crsr = conn.cursor()
        crsr.execute(cls.MAKE_RESERVATION, (id, user, proj_id, row, col))
        conn.commit()

    @classmethod
    def check_if_is_reserved(cls, conn, tpl):
        row, col = tpl
        crsr = conn.cursor()
        crsr.execute(cls.GET_RESERVED_SEATS, (row, col))
        a = crsr.fetchone()[0]
        if a != 0:
            return True
        return False

    # def print_occupied(cls, conn, tpl_lst):
    #     rows, cols = HALL_SIZE
    #     hall = [['.' for x in range(rows)] for y in range(cols)]
    #     for element in tpl_lst:
    #         x, y = element
    #         hall[x][y] = 'X'

