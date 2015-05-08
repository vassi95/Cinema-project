DB_NAME="cinema.db"
DB_DATA="test_data.sql"
SQL_FILE="create_cinema.sql"
TABLES=["Movies", "Projections", "Reservations"]
HALL_SIZE=(10,10)
# On spell show_movies - print all movies ORDERed BY rating
SHOW_MOVIES='''SELECT * FROM Movies
               ORDER BY rating '''

# On spell show_movie_projections <movie_id> [<date>] - print all projections of
# a given movie for the given date (date is optional).
SHOW_MOVIE_PROJECTION=''' SELECT Movies.name, projection_date,
                          projection_time FROM Movies
                          JOIN Projections
                          ON Movies.id=Projections.movie_id '''
