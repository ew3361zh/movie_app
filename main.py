from flask import Flask, request, render_template, redirect
#from apis import cat_img_api, cat_fact_api, cat_video_api
from apis.tmdb import get_movie_titles
#from database import db 

app = Flask(__name__)

@app.route('/')
def home_page():
    movies=get_movie_titles()
    return render_template('index.html', movies=movies)

#@app.route('/get-movie')
#def get_movie():
#    movie_titles = tmdb.


if __name__ == '__main__':
    app.run()
