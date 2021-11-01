from flask import Flask, request, render_template, redirect
from apis import omdb, tmdb, youtube_api
from database.favorites_db import FavoritesDB
from database.cached_db import CacheDB
from create_new_movie import create_new_movie
from create_new_movie import movie_info_string

app = Flask(__name__)
favorites_db = FavoritesDB() # create favorites db
movie_cache_db = CacheDB() # create cache db

@app.route('/')
def home_page():
    movies = tmdb.get_movie_titles()
    return render_template('index.html', movies = movies)


@app.route('/get-movie')
def get_movie():
    title = request.args.get('title')
    year = request.args.get('year')
    tmdb_id = request.args.get('tmdb_id')
    movie_details = omdb.get_movie_data(title, year)
    # vid_title, vid_id = youtube_api.movie_trailer(title)
    vid_title = 'vid_title'
    vid_id = 'vid_id'
    new_movie = create_new_movie(movie_details, vid_id, vid_title, tmdb_id)
    movie_details_for_display = movie_info_string(new_movie)
    new_movie_call = True
    # we need movie_info and poster
    return render_template('movie.html', newMovie=new_movie_call, videoID=vid_id, videoTitle=vid_title, title=title, year=year, poster=new_movie.poster_img, tmdb_id=tmdb_id, data=movie_details_for_display)


@app.route('/add-to-favs')
def add_movie_to_fav_db():
    
    title = request.args.get('title')
    tmdb_id = request.args.get('tmdb_id')
    year = request.args.get('year')
    movie_details = omdb.get_movie_data(title, year)
    # print(movie_details)
    # vid_title, vid_id = youtube_api.movie_trailer(title)
    vid_title = 'vid_title'
    vid_id = 'vid_id'
    favorite = create_new_movie(movie_details, vid_id, vid_title, tmdb_id)
    print(favorite)
    success = favorites_db.add_favorite(favorite) # send movie object to favorites db
    print(success)
    # using this data, add the movie to favs db
    # get the favorites list
    favorite_movie_list = favorites_db.get_all_favorites()
    # send user to favs.html
    return render_template('favs.html', favMovieList = favorite_movie_list)

@app.route('/show-fav-movie')
def show_movie_from_fav_db():
    tmdb_id = request.args.get('tmdb_id')
    # using id, get movie details from db
    title = 'get from db'
    poster = 'get from db'
    movie_data = 'get from db'
    trailer_title = 'get from db'
    video_id = 'get from db'
    new_movie_call = False
    return render_template('movie.html', title=title, data=movie_data, poster=poster, videoTitle=trailer_title, videoID=video_id, newMovie = new_movie_call)
if __name__ == '__main__':
    app.run()