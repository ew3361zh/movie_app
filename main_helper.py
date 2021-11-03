from apis import omdb, tmdb, youtube_api
from create_new_movie import create_new_movie


def assemble_selected_movie_data(title, year, tmdb_id):

    movie_details = omdb.get_movie_data(title, year)
    vid_title, vid_id = youtube_api.movie_trailer(title)
    new_movie = create_new_movie(movie_details, vid_id, vid_title, tmdb_id)
    
    return new_movie

def assemble_favorite_movie_object(title, date, tmdb_id):
    date = date.split()
    year=date[-1]
    movie_details = omdb.get_movie_data(title, year)
    vid_title, vid_id = youtube_api.movie_trailer(title)
    favorite = create_new_movie(movie_details, vid_id, vid_title, tmdb_id)
    return favorite

def show_add_to_favorites_button(favorite):
    if favorite:
        return False
    else:
        return True