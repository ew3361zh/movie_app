import requests
import os
from pprint import pprint

# order of operations:
# 1. cd to directory path
# 2a. python3 -m venv env to create virtual env 
# 2b. source env/bin/activate to switch into virtual env
# 3. pip install requests (why doesn't import requests work here?)
# 4. export OMDB_KEY=the top secret key
# 5. python filename.py to run the file

omdb_key = os.environ.get('OMDB_KEY')



def get_movie_data():  
    try: 
        movie_title = input('Please enter a movie title you would like more info on: ')
        omdb_url = f'http://www.omdbapi.com/?apikey={omdb_key}&t={movie_title}'
        movie_data = requests.get(omdb_url).json()
        pprint(movie_data)
        return movie_data
    except Exception as e:
        print('Can\'t fetch fact because', e)
