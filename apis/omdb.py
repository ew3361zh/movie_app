import requests
import os
from pprint import pprint

omdb_key = os.environ.get('OMDB_KEY')

def get_movie_data(title, release_year):  
    try: 
        omdb_url = f'http://www.omdbapi.com/?apikey={omdb_key}&t={title}&y={release_year}'
        movie_data = requests.get(omdb_url).json()
        return movie_data
    except Exception as e:
        print('Can\'t fetch fact because', e)
