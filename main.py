from flask import Flask, request, render_template, redirect
from apis import omdb, tmdb, youtube_api
from database.movie_db import MovieDB
from create_new_movie import create_new_movie
from create_new_movie import movie_info_string

app = Flask(__name__)
movie_db = MovieDB() # create the DB

@app.route('/')
def home_page():
    # get data from api, or cache and return data or none/error
    movie_dict, error= tmdb.get_movie_titles()

    if movie_dict:
        movie_list=list(movie_dict['title'])
    else:
        # an error html?????????????????????????????
        movie_list='an error has occured'
    return render_template('index.html', movieTitles = movie_list)

@app.route('/get-movie')
def get_movie():
    
    title = request.args.get('title')
    movie_dict = tmdb.get_movie_titles() # getting the initial TMDB dictionary again to be able to match release year value to selected title
    release_year = movie_dict[title] # title returned from home_page selection is used as key to extract release_year value from TMDB movie dictionary
    vid_title, vid_id = youtube_api.movie_trailer(title) # line was the same in both if and else statements (lines 24 and 34 respectively) so moved outside to reduce lines of code
    # check if movie in SQL db
    movie_check = movie_db.check_movie_in_db(title)
    if movie_check == None: # None only returned from line 22 if movie not in DB
        movie_data = omdb.get_movie_data(title, release_year) # release year from line 21 sent along with title to OMDB to ensure we get correct year movie
        # vid_title, vid_id = youtube_api.movie_trailer(title) # same as line 34 in else block and can be moved outside if/else block to line 19
        new_movie = create_new_movie(movie_data, vid_id)
        movie_db.add_movie_to_db(new_movie)
        movie_info = movie_info_string(new_movie)
        return render_template('movie.html', title=title, data=movie_info, poster=new_movie.poster_img, videoTitle=vid_title, videoID=vid_id)

    else:
        print('Movie Object')
        print(movie_check)
        movie_info = movie_info_string(movie_check)
        # vid_title, vid_id = youtube_api.movie_trailer(title)
        # we'll have a movie object from the sql db
        return render_template('movie.html', title=title, data=movie_info, poster=movie_check.poster_img, videoTitle=vid_title, videoID=movie_check.youtube_id)

if __name__ == '__main__':
    app.run()