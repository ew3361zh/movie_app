from flask import Flask, request, render_template, redirect
from apis import omdb, tmdb, youtube_api
#from database import db 

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/get-movie')
def get_movie():
    movie_titles = tmdb.get_movie_titles()
    #title = user choice
    movie_data = omdb.get_movie_data()
    movie_trailer_id = youtube_api.movie_trailer()
    movie_title = ""
    movie_poster = ""
    video_id = ""
    movie_info = ""
    return render_template('movie.html', title=movie_title, data=movie_info,poster=movie_poster, videoID=video_id)


if __name__ == '__main__':
    app.run()