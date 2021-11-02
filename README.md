# Latest Movie Releases Info App

November 2021 create by Abdifatah A. (@3bdifatah), Mohammad Z. (@sf7293gv), and Niko T. (@ew3361zh)

Uses [The Movie Database - TMDB](https://www.themoviedb.org/) API, [The Open Movie Database - OMDB](https://www.omdbapi.com/) API, and the [YouTube](https://developers.google.com/youtube/v3/docs/search/list) API.

Rendered to web app via Flask.

The top 20 latest movie theater releases in the US are queried from The Movie Database and presented to the user on the home page (index).

User clicks a button to get more info on one of the movies from this list and a host of information including an image of the movie poster, the director of the movie, some of the actors, the official movie trailer embedded YouTube video and more is all presented in a single page to the user. They have the option to add that movie to their favorites or search for info on another of the top 20 recent releases. User can then query a list of their favorites all collected in one page with the option to view the full movie info or to remove the movie from their favorites.

# To install and run

* Create a [YouTube API key](https://developers.google.com/youtube/registering_an_application). Only need an API key.
* Create an environment variable **YOUTUBE_API** to hold your key.
* Create a [TMDB API key](https://developers.themoviedb.org/3/getting-started/authentication).
* Create an environment variable **TMDB_KEY** to hold your key.
* Create a [OMDB API key](https://www.omdbapi.com/apikey.aspx).
* Create an environment variable **OMDB_KEY** to hold your key.

* Create and activate virtual environment using Python 3
* `pip install -r requirements.txt`
* `python main.py`

App will be running on http://127.0.0.1:5000