import requests
import os
from pprint import pprint
import tmdb_cache

"""
The Movie DB (https://www.themoviedb.org/?language=en-US) 
"""

tmdb_key = ''
# print(tmdb_key)

tmdb_url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=0f6e4ae275505f59ad1f7ea5b93d5f6f&language=en-US&page=1&region=US'


""" This function will return a list movies from the api """
def get_movie_titles():
    try:

        movies = tmdb_cache.get_movie_list()

        if movies:
            return movies 

        else:
            movie_data = requests.get(tmdb_url).json()
            results = movie_data['results']

            movie_data = # make API request here 

            tmdb_cache.add_movie_list(movie_data)
            return movie_data

        # for movie in results:
        #     title = movie['title']
        #     release_date = movie['release_date'] # tmdb movie release dates come in format 'yyyy-mm-dd'
        #     release_date_list = release_date.split('-') 
        #     release_year = release_date_list[0]
        #     movie_data_dict[title] = release_year
        # movie_titles = []
        # for movie in results:
        #     title = movie['title']
        #     movie_titles.append(title)

        # pprint(movie_titles)
       

    except Exception as e:
        print('Can\'t fetch movie titles because', e)