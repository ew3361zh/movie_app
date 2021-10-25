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
    
    # this seems to be the usual format for the actors field in the OMDB API response: "actor_1, actor_2, actor_3"
    # TODO add validation/error handling to this part in case there's only one actor or zero actors listed
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
    
    # TODO add add_movie_to_db(new_movie) in main immediately after this function returns the new_movie object

    return new_movie # if necessary, because data is coming from main.py already

def movie_info_string(movie_object):
    movie_info = f'Director: {movie_object[1]}\nReleased on: {movie_object[2]}\n Actors: {movie_object[3]}, {movie_object[4]}\nGenre: {movie_object[6]}\nRated: {movie_object[7]}\nPlot:{movie_object[8]}'
    return movie_info