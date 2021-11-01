import sqlite3
from .config import db_path
from datetime import datetime, date, time
# from exceptions.movie_error import MovieError

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
                cached_time = results_query.fetchone() # movie list has 4 elements {title, year, id, cached_time}
                if cached_time:
                    if current_time - cached_time.time_cached > MAX_AGE_SECONDS or cached_time == None:
                        print('got here at least') 
                        conn.execute('DELETE FROM movies_cache') # results are old, clear them out - doesn't need the *, will just delete everything from this table
                    else:
                        results_query = conn.execute('SELECT * FROM movies_cache')
                        movies_list = results_query.fetchall() # need to check what this returns
                        # return movies_list, None
                        return movies_list, None #TODO returning movies_list, None seems to be allowing for None, maybe by this point we should only be getting here if there are movies in the cached_db
                else:
                    return None
                # else:
                #     results_query = conn.execute('SELECT * FROM movies_cache')
                #     movies_list = results_query.fetchall() # need to check what this returns
                #     # return movies_list, None
                #     return movies_list, None #TODO returning movies_list, None seems to be allowing for None, maybe by this point we should only be getting here if there are movies in the cached_db
            except Exception as e:
                return None, 'Error connecting to TMBD API because' + str(e)
                # raise MovieError('Problem fetching cached movies list from db')
                # pass
    
    def add_movie_list_cache(self, movie_list):
        # print(movie_list)
        current_time = datetime.now().timestamp()
        with sqlite3.connect(db) as conn:
            try:
                conn.execute('DELETE FROM movies_cache') # just to be safe, deleting previous cache. Ideally only want this to be called after data has been proven too old or doesn't exist in table yet
                print(movie_list)
                for movie in movie_list:
                    
                    conn.executemany(f'INSERT INTO movies_cache VALUES(?, ?, ?, ?)',
                                (movie.title, movie.year, movie.id, current_time)) # check if same as Abdi's key names in movie_list objects
                # conn.row_factory = sqlite3.Row
                # results_query = conn.execute('SELECT * FROM movies_cache')
                # movies_list = results_query.fetchall()
                # for movie in movies_list:
                #     print(movie)

            # except:
            #     # pass
            #     raise MovieError('Problem adding movie list to cache db')
            except Exception as e:
                return None, 'Error connecting to TMBD API because' + str(e)