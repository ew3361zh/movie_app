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

    movie_details = omdb.get_movie_data(title, release_year)  # behind the scenes, cache check will occur 
    vid_title, vid_id = youtube_api.movie_trailer(title) # line was the same in both if and else statements (lines 24 and 34 respectively) so moved outside to reduce lines of code

    return render_template('movie.html', title=title, data=movie_info, poster=new_movie.poster_img, videoTitle=vid_title, videoID=vid_id)


# todo add to favorites route

# todo favorites page


if __name__ == '__main__':
    app.run()