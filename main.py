from flask import Flask, request, render_template, redirect
from apis import omdb, tmdb, youtube_api
from database.movie_db import MovieDB
from create_new_movie import create_new_movie
from create_new_movie import movie_info_string

app = Flask(__name__)
movie_db = MovieDB() # create the DB

@app.route('/')
def home_page():
    movie_titles = tmdb.get_movie_titles()
    return render_template('index.html', movieTitles = movie_titles)

@app.route('/get-movie')
def get_movie():
    
    title = request.args.get('title')
    # check if movie in SQL db
    movie_check = movie_db.check_movie_in_db(title)
    if movie_check == None: # None only returned from line 22 if movie not in DB
        movie_data = omdb.get_movie_data(title)
        vid_title, vid_id = youtube_api.movie_trailer(title)
        new_movie = create_new_movie(movie_data, vid_id)
        movie_db.add_movie_to_db(new_movie)
        movie_info = movie_info_string(new_movie)
        return render_template('movie.html', title=title, data=movie_info, poster=new_movie.poster_img, videoTitle=vid_title, videoID=vid_id)

    else:
        print('Movie Object')
        print(movie_check)
        movie_info = movie_info_string(movie_check)
        # we'll have a movie object from the sql db
        return render_template('movie.html', title=title, data=movie_info, poster=movie_check.poster_img, videoTitle='db', videoID=movie_check.youtube_id)

if __name__ == '__main__':
    app.run()