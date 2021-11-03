import sqlite3
from .config import db_path
from model.movie_model import Movie
from exceptions.movie_error import MovieError

db = db_path

class MovieDB():
    
    def __init__(self):
        #create table function
        with sqlite3.connect(db) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS movies (
                        title TEXT NOT_NULL UNIQUE,
                        director TEXT,
                        release_date TEXT,
                        actor_1 TEXT,
                        actor_2 TEXT,
                        poster_img TEXT,
                        genre TEXT,
                        rating TEXT,
                        plot_summary TEXT,
                        youtube_id TEXT)"""
            )
        # conn.close()
    
    def check_movie_in_db(self, title):
        # check if movie title selected is already in db, return whole movie object if it is
        with sqlite3.connect(db) as conn:
            try:
                results_query = conn.execute('SELECT * FROM movies WHERE title = ?', (title,))
                results = results_query.fetchone()
                if results == None:
                    return None # or return False/True
                else:
                    requested_movie = Movie(results[0],
                                            results[1],
                                            results[2],
                                            results[3],
                                            results[4],
                                            results[5],
                                            results[6],
                                            results[7],
                                            results[8],
                                            results[9]
                                            )
                    return requested_movie
            except:
                raise MovieError('Problem fetching movie from db')
    # add movie
    def add_movie_to_db(self, movie):
        # add a movie to the db assuming it's not in db (title field is unique)
        with sqlite3.connect(db) as conn:
            try:
                conn.execute(f'INSERT INTO movies VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                            (movie.title,
                            movie.director,
                            movie.release_date,
                            movie.actor_1,
                            movie.actor_2,
                            movie.poster_img,
                            movie.genre,
                            movie.rating,
                            movie.plot_summary,
                            movie.youtube_id))
            except:
                raise MovieError('Problem adding movie to db')

