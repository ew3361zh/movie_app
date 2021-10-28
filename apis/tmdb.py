import requests
import os
from database.movie_db import MovieDB
from pprint import pprint

"""
The Movie DB (https://www.themoviedb.org/?language=en-US) 
"""

tmdb_key = os.environ.get('TMDB_KEY')
# print(tmdb_key)

tmdb_url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=0f6e4ae275505f59ad1f7ea5b93d5f6f&language=en-US&page=1&region=US'


""" This function will return a list movies from the api """
def get_movie_titles():
    try:
        #check if recent movie list in cache
        movies = movie_db.check_cache_for_movie_list()

        # if movies in cache return it
        if movies:
            return movies

        #else fetch data from api then return data
        else:
            movie_data = requests.get(tmdb_url).json()
            results = movie_data['results']
            movie_list =[]
            
            for movie in results:
                title=movie['title']
                release_date = movie['release_date'] # tmdb movie release dates come in format 'yyyy-mm-dd'
                release_date_list = release_date.split('-') 
                release_year = release_date_list[0]
                tmdb_id = movie['id']

                movie_list.append({'title': title, 'year': release_year, 'id': tmdb_id})
            
            #store it in cache
            Movie_db.add_movie_list(movie_list)
            return movie_list
    except Exception as e:
        print('Can\'t fetch movie titles because', e)