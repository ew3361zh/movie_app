# take omdb_api json response and youtube_api from main to build new movie object
# return object back to main for display in flaskApp (or not necessary because data is already available in main?)
# send new movie object to movie_db add_new_movie function

from exceptions.movie_error import MovieError
from model.movie_model import Movie
from database.movie_db import movie_db

def create_new_movie(omdb_data, youtube_video_id):
    # TODO make sure this function is called in main and data is sent with a return object set up to get the new movie object
    # function takes data from main.py to create new movie object
    # if this function is called, it means the secondary apis (OMDB and YouTube) have been called
    # which means the original title chosen by the user was checked in the db
    
    actors = omdb_data['Actors']
    actors_list = actors.split(', ')
    actor_1 = actors_list[0]
    actor_2 = actors_list[1]

    
    new_movie = Movie(omdb_data['Title'],
                    omdb_data['Director'],
                    omdb_data['Released'],
                    actor_1,
                    actor_2,
                    omdb_data['Poster'],
                    omdb_data['Genre'],
                    omdb_data['Rated'],
                    omdb_data['Plot'],
                    youtube_video_id)
    
    add_movie_to_db(new_movie)

    return new_movie # if necessary, because data is coming from main.py already