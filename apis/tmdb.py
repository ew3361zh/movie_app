import requests
import os
from pprint import pprint
import main_helper
from main import movie_cache_db

"""
The Movie DB (https://www.themoviedb.org/?language=en-US) 
"""

tmdb_key = os.environ.get('TMDB_KEY')
tmdb_url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={tmdb_key}&language=en-US&page=1&region=US'


""" This function will return a list movies from the api """
def get_movie_titles():
    
    try:
        movies = movie_cache_db.check_cache()
        
        if movies:

            return movies
        else:
            movie_json = get_movie_data_from_api()
            if movie_json:
                movie_list = add_titles_to_list(movie_json)

                #store it in cache
                movie_cache_db.add_movie_list_cache(movie_list)
                return movie_list
            else:
                pass


    except Exception as e:
        return None, 'Error getting list of movies from cache and/or TMDB API' + str(e)


def get_movie_data_from_api():
    try:
        movie_data = requests.get(tmdb_url).json()
        return movie_data, None
    except Exception as e:
        return None, 'Error connecting to TMBD API because' + str(e)


def add_titles_to_list(movie_data):

    movie_list =[]  
    results = movie_data[0]['results']
    for movie in results:
        title = movie['title']
        release_date = movie['release_date'] # tmdb movie release dates come in format 'yyyy-mm-dd'
        release_date_list = release_date.split('-') 
        release_year = release_date_list[0]
        tmdb_id = movie['id']

        movie_list.append({'title': title, 'year': release_year, 'id': tmdb_id})


    return movie_list