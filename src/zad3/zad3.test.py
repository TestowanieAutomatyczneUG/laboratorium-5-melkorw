import unittest
from zad3 import Song

class SongTest(unittest.TestCase):
    def setUp(self):
        self.temp = Song()

    
    def tearDown(self):
        self.temp = None