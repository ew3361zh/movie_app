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
    movie_data = omdb.get_movie_data()
    movie_trailer_id = youtube_api.movie_trailer()

if __name__ == '__main__':
    app.run()
