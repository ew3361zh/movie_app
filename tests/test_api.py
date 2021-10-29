import unittest 
from apis import omdb, tmdb, youtube_api

class TestTMDB(unittest.TestCase):
    
    def test_get_movie_list(self):
        movies = tmdb.get_movie_titles()
        self.assertIsNotNone(movies)


# class TestCatFact(unittest.TestCase):

#     def test_get_cat_fact(self):
#         fact = cat_fact_api.get_random_fact()
#         self.assertIsNotNone(fact)

#         # TODO more meaningful tests