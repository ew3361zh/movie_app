import sqlite3
from .config import db_path
from exceptions.movie_error import MovieError

db = db_path
MAX_AGE_SECONDS = 30 # tbd actual time we should use

class CacheDB():

    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS movies_cache (
                            title TEXT NOT_NULL,
                            release_year TEXT,
                            tmdb_id TEXT NOT NULL,
                            time_cached INTEGER NOT NULL)"""
                        )

    def check_cache(self):
        # function checks current time, gets time-cached from DB, makes assessment based on MAX_AGE_SECONDS variable on whether data is fresh enough
        current_time = datetime.now().timestamp()
        with sqlite3.connect(db) as conn:
            try:
                conn.row_factory = sqlite3.Row
                results_query = conn.execute('SELECT * FROM movies_cache LIMIT 1')
                cached_time = results_query.fetchone().time_cached # movie list has 4 elements {title, year, id, cached_time}
                if current_time - cached_time > MAX_AGE_SECONDS: 
                    conn.execute('DELETE FROM movies_cache') # results are old, clear them out - doesn't need the *, will just delete everything from this table
                #     return None # made up amount of seconds for testing if this works
                # elif cached_time == None: # return none if movielist cache hasn't yet been added
                #     return None
                else:
                    results_query = conn.execute('SELECT * FROM movies_cache')
                    movies_list = results_query.fetchall() # need to check what this returns
                    return movies_list 
            except:
                raise MovieError('Problem fetching cached movies list from db')
    
    def add_movie_list_cache(self, movie_list):
        current_time = datetime.now().timestamp()
        with sqlite3.connect(db) as conn:
            try:
                conn.execute('DELETE FROM movies_cache') # just to be safe, deleting previous cache. Ideally only want this to be called after data has been proven too old or doesn't exist in table yet
                for movie in movies_list:
                    conn.execute(f'INSERT INTO movies_cache VALUES(?, ?, ?, ?)',
                                (movie.id, movie.title, movie.year, current_time)) # check if same as Abdi's key names in movie_list objects
            except:
                raise MovieError('Problem adding movie list to cache db')
