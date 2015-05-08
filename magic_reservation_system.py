#!/usr/bin/env python3
import sqlite3
from movies import Movie

conn = sqlite3.connect('cinema.db')


def show_movies():
    print('Current movies:')
    mov = Movie.show_movies(conn)
    for row in mov:
        print('{[]}-{}-{()}'.format(row[0], row[1], row[2]))


def show_movie_projections(movie_id):
    print('Projections for movie:')
    cursor = conn.cursor()
    result = cursor.execute("SELECT Movies.name, projection_date, projection_time \
        FROM Movies JOIN Projections \
        ON Movies.id=Projections.movie_id ")
    for row in result:
        print('{}-{}-{}'.format(row[0], row[1], row[2]))


def make_reservation():
    name = input("Step 1 (User): Enter name>")
    if name == 'give_up':
        return
    tickets = input("Step 1 (User): Enter number of tickets>")
    if tickets == 'give_up':
        return
    else:
        tickets = int(tickets)
        show_movies()
    movie_id = input("Step 2 (Movie): Choose a movie>")
    if movie_id == 'give_up':
        return
    else:
        show_movie_projections(movie_id)
    projection_id = input("Step 3 (Projection): Choose a projections>")
    if projection_id == 'give_up':
        return
    print('Available seats (marked with a dot):')
    # sth that prints the available seats
    # function which makes the seats occuiped
    chosen_seats = []
    for ticket in range(tickets):
        seat_free = False
        while not seat_free:
            chosen = input("Step 4 (Seats): Choose seat {}>".format(ticket + 1))
            if chosen == 'give_up':
                return
            chosen = tuple(int(x.strip()) for x in chosen.split(','))
            # if the seat is occupied:print('This seat is already taken!')
            # proverka za pove4e ot 10 na shirina i visochina na masiva elif chosen[0] > 10
            # or chosen[0] < 1 or chosen[1] > 10 or chosen[1] < 1:print('Cinema is 10x10!') else:
            seat_free = True
            # adds to occupied .append(chosen)
            chosen_seats.append(chosen)
    # printing the reservation
    confirmation = input('Step 5 (Confirm - type "finalize") >')
    if confirmation == 'give_up':
        return
    if confirmation == 'finalize':
        for seat in chosen_seats:
            # make new reservation (name, projection_id, seat[0], seat[1])
            print('Thanks! Enjoy the movie!')


def exit():
    import sys
    print('Goodbye!')
    sys.exit()


def show_help():
    print('The following commands are available:')
    print('- "show_movies" - Prints all movies ordered by rating')
    print('- "show_movie_projections <movie_id> [<date>]" - Prints all projections of a given movie for the given date (date is optional).')
    print('- "make_reservation" - You can choose a movie and reserve seats')
    print('- "cancel_reservation <name>" - You can cansel a reservation')
    print('- "exit" - Leave the menu')


def main():
    print(show_movies())

if __name__ == '__main__':
    main()
