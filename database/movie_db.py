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
        
            conn.execute("""CREATE TABLE IF NOT EXISTS movies_cache (
                        title TEXT NOT_NULL,
                        release_year TEXT,
                        tmdb_id TEXT NOT NULL,
                        time_cached INTEGER NOT NULL)"""
            )

        # conn.close()
    
    def check_cache_for_movie_list(self):

        current_time = datetime.now().timestamp()
        with sqlite3.connect(db) as conn:
            try:
                results_query = conn.execute('SELECT * FROM movies_cache LIMIT 1')
                cached_time = results_query.fetchone()[3] # movie list has 4 elements {title, year, id, cached_time}
                if current_time - cached_time > 30: 
                    conn.execute('DELETE FROM movies_cache') # results are old, clear them out - doesn't need the *, will just delete everything from this table
                    return None # made up amount of seconds for testing if this works
                elif cached_time == None: # return none if movielist cache hasn't yet been added
                    return None
                else:
                    results_query = conn.execute('SELECT * FROM movies_cache')
                    movies_list = results_query.fetchall()
                    return movies_list 
            except:
                raise MovieError('Problem fetching cached movies list from db')    

                    
    def add_movie_list(self, movie_list):
        current_time = datetime.now().timestamp()
        with sqlite3.connect(db) as conn:
            try:
                conn.execute('DELETE FROM movies_cache') # just to be safe, deleting previous cache. Ideally only want this to be called after data has been proven too old or doesn't exist in table yet
                for movie in movies_list:
                    conn.execute(f'INSERT INTO movies_cache VALUES(?, ?, ?, ?)',
                                (movie.id, movie.title, movie.year, current_time)) # check if same as Abdi's key names in movie_list objects
            except:
                raise MovieError('Problem adding movie list to cache db')

    # add movie
    def add_movie_to_db(self, movie):
        # add a movie to the db assuming it's not in db (title field is unique)
        # TODO write test to make sure it's not adding a movie that's already in the DB
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
                # conn.close()
            except:
                raise MovieError('Problem adding movie to db')
    
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

