import sqlite3
from .config import db_path
from model.movie_model import Favorite
from exceptions.movie_error import MovieError

db = db_path

class FavoritesDB():
    
    def __init__(self):
        #create table function
        with sqlite3.connect(db) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS favorites (
                        tmdb_id TEXT NOT NULL UNIQUE, 
                        title TEXT NOT_NULL,
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


    # fetch all favorite movies from db
    def get_all_favorites(self):

        with sqlite3.connect(db) as conn:
            try:
                conn.row_factory = sqlite3.Row
                results_query = conn.execute(f'SELECT * FROM favorites')
                all_favorites = results_query.fetchall()
                return all_favorites
            except:
                raise MovieError('Problem fetching all favorites')

    # add movie to favorites db
    def add_favorite(self, movie):
        # TODO make sure movie object sent here is getting tmdb_id
        # TODO write test to make sure it's not adding a movie that's already in the DB
        check_movie = check_movie_in_db(movie.title)
        if check_movie == None: 
            with sqlite3.connect(db) as conn:
                try:
                    conn.execute(f'INSERT INTO favorites VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                (movie.tmdb_id,
                                movie.title,
                                movie.director,
                                movie.release_date,
                                movie.actor_1,
                                movie.actor_2,
                                movie.poster_img,
                                movie.genre,
                                movie.rating,
                                movie.plot_summary,
                                movie.youtube_id))
                    return True
                except:
                    raise MovieError('Problem adding favorite to db')
        else:
            return False
    
    #TODO delete favorite from DB function
    
    def check_movie_in_db(self, title):
        # check if movie title selected is already in db, return whole movie object if it is
        with sqlite3.connect(db) as conn:
            try:
                conn.row_factory = sqlite3.Row
                results_query = conn.execute('SELECT * FROM favorites WHERE title = ?', (title,))
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

