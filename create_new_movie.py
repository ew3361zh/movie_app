# take omdb_api json response and youtube_api from main to build new movie object
# return object back to main for display in flaskApp (or not necessary because data is already available in main?)
# send new movie object to movie_db add_new_movie function

from exceptions.movie_error import MovieError
from model.movie_model import Favorite
# from database.movie_db import movie_db

def create_new_movie(omdb_data, youtube_video_id, youtube_video_title, tmdb_id):

    # this seems to be the usual format for the actors field in the OMDB API response: "actor_1, actor_2, actor_3"
    # TODO add validation/error handling to this part in case there's only one actor or zero actors listed
    actors = omdb_data['Actors']
    actors_list = actors.split(', ')
    actor_1 = actors_list[0]
    actor_2 = actors_list[1]

    
    new_movie = Favorite(tmdb_id,
                    omdb_data['Title'],
                    omdb_data['Director'],
                    omdb_data['Released'],
                    actor_1,
                    actor_2,
                    omdb_data['Poster'],
                    omdb_data['Genre'],
                    omdb_data['Rated'],
                    omdb_data['Plot'],
                    youtube_video_title,
                    youtube_video_id)

    return new_movie 

def movie_info_string(movie_object):
    #movie_info = f'Director: {movie_object[1]}\nReleased on: {movie_object[2]}\n Actors: {movie_object[3]}, {movie_object[4]}\nGenre: {movie_object[6]}\nRated: {movie_object[7]}\nPlot:{movie_object[8]}'
    movie_info = f'Director: {movie_object.director}\nReleased on: {movie_object.release_date}\n Actors: {movie_object.actor_1}, {movie_object.actor_2}\nGenre: {movie_object.genre}\nRated: {movie_object.rating}\nPlot:{movie_object.plot_summary}'
    return movie_info