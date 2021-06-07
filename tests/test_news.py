import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    def setUp(self):
        '''
        test to run before each test
        '''
        self.news_sources=News('abc-au', "ABC News",'https://abcnews.go.com')

    def test_instance(self):
        '''
        test case to confirm the object is an instance of the news
        '''
        self.assertTrue(isinstance(self.news_sources,News))

    def test_init(self):
        '''
        test case to confirm the object is initialised correctly
        '''
        self.assertEqual(self.news_sources.id,"abc-au")
        self.assertEqual(self.news_sources.name, "ABC News")
        self.assertEqual(self.news_sources.url, "https://abcnews.go.com")

