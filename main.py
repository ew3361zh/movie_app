from flask import Flask, request, render_template, redirect
from apis import omdb, tmdb, youtube_api
from database.movie_db import MovieDB
from create_new_movie import create_new_movie
from create_new_movie import movie_info_string

app = Flask(__name__)
movie_db = MovieDB() # create the DB

@app.route('/')
def home_page():
    print('hi')
    movie_titles = tmdb.get_movie_titles()
    
    #print(movie_titles)
    return render_template('index.html', movieTitles = movie_titles)

@app.route('/get-movie')
def get_movie():
    
    title = request.args.get('title')
    print(title)
    # check if movie in SQL db
    movie_check = movie_db.check_movie_in_db(title)
    if movie_check == None: # None only returned from line 22 if movie not in DB
        movie_data = omdb.get_movie_data(title)
        movie_trailer_id = youtube_api.movie_trailer(title)
        new_movie = create_new_movie(movie_data, movie_trailer_id)
        movie_db.add_movie_to_db(new_movie)
        movie_info = movie_info_string(new_movie)
    else:
        movie_check.title
        # we'll have a movie object from the sql db

    return render_template('movie.html', title=title, data=movie_info, poster=new_movie.poster_img, videoID=new_movie.youtube_id)

if __name__ == '__main__':
    app.run()