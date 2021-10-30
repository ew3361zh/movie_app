import unittest 

import app

class TestHomePage(unittest.TestCase):

    def test_get_home_page(self):
        with app.app.test_client() as client:
            response = client.get('/')
            self.assertEqual(200, response.status_code)

        # TODO more meaningful tests