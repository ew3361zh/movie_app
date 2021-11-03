from flask import Flask, request, render_template, redirect
from apis import omdb, tmdb, youtube_api
from database.favorites_db import FavoritesDB
from database.cached_db import CacheDB
from create_new_movie import create_new_movie
from create_new_movie import movie_info_string
from main_helper import *

app = Flask(__name__)
favorites_db = FavoritesDB() # create favorites db
movie_cache_db = CacheDB() # create cache db

@app.route('/')
def home_page():
    # this function queries tmdb api or cache if exists to get initial list of movie titles for display on home index page
    movies = tmdb.get_movie_titles()
    return render_template('index.html', movies = movies)


@app.route('/favorites')
def favorites_page():
    # this function returns a list of favorite movies stored in the favorites db
    favorite_movie_list = favorites_db.get_all_favorites()
    return render_template('favs.html', favMovieList = favorite_movie_list)


@app.route('/get-movie')
def get_movie():
    # this function takes selected movie info sent from home_page to query OMDB api and youtube api to assemble pieces for a full movie object
    title = request.args.get('title')
    year = request.args.get('year')
    tmdb_id = request.args.get('id')
    new_movie = assemble_selected_movie_data(title, year, tmdb_id)
    show_or_not = show_add_to_favorites_button(favorites_db.get_one_favorite(tmdb_id))
    
    return render_template('movie.html', new_movie_call=show_or_not, movie_object=new_movie)


@app.route('/add-to-favs')
def add_movie_to_fav_db():
    
    title = request.args.get('title')
    tmdb_id = request.args.get('tmdb_id')
    year = request.args.get('year')
    favorite = assemble_favorite_movie_object(title, year, tmdb_id)
    success = favorites_db.add_favorite(favorite)
    favorite_movie_list = favorites_db.get_all_favorites()

    return render_template('favs.html', favMovieList = favorite_movie_list)

@app.route('/show-fav-movie')
def show_movie_from_fav_db():
    tmdb_id = request.args.get('id')
    fav_from_db = favorites_db.get_one_favorite(tmdb_id)
    fav_details = movie_info_string(fav_from_db)
    new_movie_call = False

    return render_template('movie.html', movie_object=fav_from_db, new_movie = new_movie_call)


@app.route('/delete_movie')
def delete_movie():
    tmdb_id = request.args.get('id')
    favorites_db.delete_favorite(tmdb_id)
    favorite_movie_list = favorites_db.get_all_favorites()

    return render_template('favs.html', favMovieList = favorite_movie_list)

if __name__ == '__main__':
    app.run()