import unittest
from src.seo_optimization import optimize_seo

class TestSeoOptimization(unittest.TestCase):

    def setUp(self):
        self.article = {
            'title': 'AI in News Industry',
            'content': 'Artificial Intelligence is revolutionizing the news industry...',
            'link': 'https://example.com/ai-in-news'
        }

    def test_optimize_seo(self):
        meta_description, keywords = optimize_seo(self.article)
        
        # Test if meta description is a string and not empty
        self.assertIsInstance(meta_description, str)
        self.assertTrue(len(meta_description) > 0)

        # Test if keywords is a list and not empty
        self.assertIsInstance(keywords, list)
        self.assertTrue(len(keywords) > 0)

        # Test if the keywords are relevant to the article content
        self.assertTrue(any(keyword in self.article['content'] for keyword in keywords))

if __name__ == '__main__':
    unittest.main()