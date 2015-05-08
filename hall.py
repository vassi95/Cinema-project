#!/usr/bin/env python3
from settings import HALL_SIZE


class Hall:
    def __init__(self, size=HALL_SIZE):
        rows, columns = size
        self.hall = [['.' for x in range(rows+1)] for y in range(columns+1)]

    def reserve_spot(self, spot):
        row, column = spot
        self.hall[row][column] = 'X'
