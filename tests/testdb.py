import unittest 
from database import db


class TestDatbase(unittest.TestCase):

    def test_store_data(self):
        is_stored = db.store_data('example')
        self.assertEqual('ok!', is_stored)
        
        # TODO more meaningful tests