import sqlite3
from .config import db_path
from model.movie_model import Movie
from exceptions.movie_error import MovieError

db = db_path

class MovieDB():

    #def create_table
    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS movies (
                        title TEXT NOT_NULL,
                        director TEXT,
                        release_date TEXT,
                        actor_1 TEXT,
                        actor_2 TEXT,
                        poster_img TEXT,
                        genre TEXT,
                        rating TEXT,
                        plot_summary TEXT,
                        youtube_link TEXT)"""
            )
        conn.close()
    
