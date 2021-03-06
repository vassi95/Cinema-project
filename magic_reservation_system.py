#!/usr/bin/env python3
import sqlite3
from movies import Movie
from projections import Projection
from reservation import Reservation
from comands import Commands
from settings import HALL_SIZE

conn = sqlite3.connect('cinema.db')


def show_movies():
    print('\nCurrent movies:\n')
    mov = Movie.show_movies(conn)
    for row in mov:
        print('[{}]-{}-({})'.format(row[0], row[1], row[2]))


def show_movie_projections(movie_id):
    print('Projections for movie:\n')
    proj = Projection.get_projection_from_db(conn, (movie_id))
    for row in proj:
        print('[{}]-{}-{}'.format(row[0], row[1], row[2]))

def is_valid_seat(row, col):
    hall_rows, hall_cols = HALL_SIZE
    return row in range(1, hall_rows +1) and col in range(1, hall_cols + 1)

def chose_seats(tickets, projection):
    occupied_seats = []

    for ticket in range(tickets):
        seat_occupied = False
        while not seat_occupied:
            print('Available seats(marked with dots)')
            chosen = input("Step 4 (Seats): Choose seat {}>".format(ticket+1))
            if chosen == 'give_up':
                return None

            chosen = tuple(int(x.strip()) for x in chosen.split(','))
            if Reservation.is_reserved(conn, chosen):
                print('This seat is already taken!')
                continue
            elif not is_valid_seat(chosen[0], chosen[1]):
                print('Cinema is 10x10!')
                continue
            else:
                seat_occupied = True
                occupied_seats.append(chosen)

    return occupied_seats

def reservation(movie_id, projection_id, seats):
    movie = Movie.get_movie(conn, movie_id)
    projection = Projection.get_projection_by_id(conn, projection_id)
    print('This is your reservation: ')
    print("Movie: {} ({})".format(movie[0], movie[1]))
    print("Date and Time: {} {} ({})".format(projection[0], projection[1],
                                             projection[2]))
    print("Seats: {}".format(seats))

def make_reservation():
    name = input("Step 1 (User): Enter name> ")
    if name == 'give_up':
        return None

    tickets = input("Step 1 (User): Enter number of tickets> ")
    if tickets == 'give_up':
        return None
    else:
        tickets = int(tickets)

    show_movies()

    movie_id = input("Step 2 (Movie): Choose a movie> ")
    if movie_id == 'give_up':
        return
    else:
        movie_id = int(movie_id)

    show_movie_projections(movie_id)

    projection_id = input("Step 3 (Projection): Choose a projections> ")
    print(Reservation.print_occupied(conn, projection_id))
    if projection_id == 'give_up':
        return None

    projection_id = int(projection_id)

    seats = chose_seats(tickets, projection_id)
    if seats:
        reservation(movie_id, projection_id, seats)

    confirmation = input('Step 5 (Confirm - type "finalize") >')
    if confirmation == 'give_up':
        return
    if confirmation == 'finalize':
        for seat in seats:
            Reservation.reserve(conn, (name, projection_id, seat[0], seat[1]))
        print('Thanks! Enjoy the movie!')


def create_commands():
    c = Commands()
    c.add_commands('show_movies', show_movies)
    c.add_commands('show_movie_projections', show_movie_projections)
    c.add_commands('make_reservation', make_reservation)
    c.add_commands('cancel_reservation', cancel_reservation)
    c.add_commands('exit', exit)
    c.add_commands('show_help', show_help)
    return c


def cancel_reservation(name, projection_id):
    Reservation.delete_reservation(conn, name, projection_id)
    print('Reservation on the name of {} was canceled.'.format(name))


def exit():
    import sys
    print('Goodbye!')
    sys.exit()


def show_help():
    print('''The following commands are available:\n
    --> "show_movies" - Prints all movies ordered by rating
    --> "show_movie_projections <movie_id> [<date>]" - Prints all projections of a given movie for the given date (date is optional).
    --> "make_reservation" - You can choose a movie and reserve seats
    --> "cancel_reservation <name> <projection_id>" - You can cansel a reservation
    --> "exit" - Leave the menu''')

def main():
    print('\n\n\t\tWellcome to our cinema! Choose one of the options:\n\n')
    show_help()
    print('\n')
    commands = create_commands()
    while 1:
        command = input('>')
        commands.run(command)

if __name__ == '__main__':
    main()
