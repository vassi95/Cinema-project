DROP TABLE IF EXISTS Movies;

CREATE TABLE Movies(id INTEGER UNIQUE PRIMARY KEY NOT NULL,
                    name TEXT
                    rating real);

DROP TABLE IF EXISTS Projections;
CREATE TABLE Projections(id INTEGER UNIQUE PRIMARY KEY NOT NULL,
                         movie_id INTEGER,
                         projection_type TEXT,
                         projection_date TEXT,
                         projection_time TEXT,
                         FOREIGN KEY(movie_id) REFERENCES Movies(id));

DROP TABLE IF EXISTS Reservations; 
CREATE TABLE Reservations(id INTEGER UNIQUE PRIMARY KEY NOT NULL, 
                          username TEXT,
                          projection_id INTEGER, 
                          row INTEGER, 
                          col INTEGER,
                          FOREIGN KEY(projection_id) REFERENCES Projections(id));
