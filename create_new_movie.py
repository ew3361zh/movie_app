# take omdb_api json response and youtube_api from main to build new movie object
# return object back to main for display in flaskApp (or not necessary because data is already available in main?)
# send new movie object to movie_db add_new_movie function
from pprint import pprint
from exceptions.movie_error import MovieError
from model.movie_model import Favorite

def create_new_movie(omdb_data, youtube_video_id, youtube_video_title, tmdb_id):

    # this seems to be the usual format for the actors field in the OMDB API response: "actor_1, actor_2, actor_3"
    actors = omdb_data['Actors']
    
    if actors != "N/A":
        actors_list = actors.split(', ')
        actor_1 = actors_list[0]
        actor_2 = actors_list[1]
    else:
        actor_1 = 'None'
        actor_2 = 'None'
    
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
