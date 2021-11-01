import requests
import os
from pprint import pprint
import main_helper
from main import movie_cache_db

"""
The Movie DB (https://www.themoviedb.org/?language=en-US) 
"""

tmdb_key = os.environ.get('TMDB_KEY')
# print(tmdb_key)
tmdb_url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={tmdb_key}&language=en-US&page=1&region=US'


""" This function will return a list movies from the api """
def get_movie_titles():
    
    try:
        # movies, None = CacheDB.check_cache() having None was erroring
        # movies, error = CacheDB.check_cache()
        # movies = main_helper.check_cache_db_helper()
        movies = movie_cache_db.check_cache()
        
        if movies:
            # for movie in movies:
            #     print(movie[0])
            return movies
        else:
            # movie_json, None = get_movie_from_api() None erroring, replaced with error as second return value
            # movie_json, error = get_movie_from_api()
            movie_json = get_movie_data_from_api()
            # pprint(movie_json)
            if movie_json:
                movie_list = add_titles_to_list(movie_json)

                #store it in cache
                # main_helper.send_movie_list_to_db(movie_list)
                movie_cache_db.add_movie_list_cache(movie_list)
                # pprint(movie_list)
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
        # print(title)
        release_date = movie['release_date'] # tmdb movie release dates come in format 'yyyy-mm-dd'
        release_date_list = release_date.split('-') 
        release_year = release_date_list[0]
        tmdb_id = movie['id']

        movie_list.append({'title': title, 'year': release_year, 'id': tmdb_id})


    return movie_list