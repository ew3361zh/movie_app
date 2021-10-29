from flask import Flask, request, render_template, redirect
from apis import omdb, tmdb, youtube_api
from database.movie_db import MovieDB
from create_new_movie import create_new_movie
from create_new_movie import movie_info_string

app = Flask(__name__)
movie_db = MovieDB() # create the DB

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
    vid_title, vid_id = youtube_api.movie_trailer(title)
    # we need movie_info and poster
    return render_template('movie.html', title=title, data=movie_details, poster=movie_details, videoTitle=vid_title, videoID=vid_id)


@app.route('/add-to-favs')
def show_favs():
    title = request.args.get('title')
    poster = request.args.get('poster')
    movie_data = request.args.get('data')
    trailer_title = request.args.get('videoTitle')
    video_id = request.args.get('videoID')
    # using this data, add the movie to favs
    # get the favorites list
    favorite_movie_list = []
    # send user to favs.html
    return render_template('favs.html', favMovieList = favorite_movie_list)
if __name__ == '__main__':
    app.run()