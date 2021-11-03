from apis import omdb, tmdb, youtube_api
from create_new_movie import create_new_movie
from create_new_movie import movie_info_string
# from database.favorites_db import FavoritesDB


def assemble_selected_movie_data(title, year, tmdb_id):
    movie_details = omdb.get_movie_data(title, year)
    vid_title, vid_id = youtube_api.movie_trailer(title)
    new_movie = create_new_movie(movie_details, vid_id, vid_title, tmdb_id)
    

    return new_movie

def assemble_favorite_movie_object(title, year, tmdb_id):
    movie_details = omdb.get_movie_data(title, year)
    vid_title, vid_id = youtube_api.movie_trailer(title)
    favorite = create_new_movie(movie_details, vid_id, vid_title, tmdb_id)
    return favorite
    