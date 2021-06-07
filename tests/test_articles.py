
import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):

    def setUp(self):
        '''
        test case to run before each test
        '''
        self.news_articles=Articles("Black Barbecue Gets Its Due in an Inspiring New Cookbook", "Joe Ray", "The first book from renowned pitmaster...", "2021-06-05T13:00:00Z", "https://media.wired.com/photos/60ba605dd9be3d", "https://www.wired.com/story/rodney-scotts-world-of-bbq/")


    def test_instance(self):
        self.assertEqual(isinstance(self.news_articles, Articles))

    def test_init(self):
        '''
        test case to confirm the object is initialised correctly
        '''
        self.assertEqual(self.news_articles.title , "Black Barbecue Gets Its Due in an Inspiring New Cookbook")
        self.assertEqual(self.news_articles.author , "Joe Ray")
        self.assertEqual(self.news_articles.description, "The first book from renowned pitmaster...")
        self.assertEqual(self.news_articles.publishedAt, "2021-06-05T13:00:00Z")
        self.assertEqual(self.news_articles.urlToImage, "https://media.wired.com/photos/60ba605dd9be3d")
        self.assertEqual(self.news_articles.url, "https://www.wired.com/story/rodney-scotts-world-of-bbq/")
        
