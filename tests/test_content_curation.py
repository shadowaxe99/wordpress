```python
import unittest
from src.content_curation import curate_content

class TestContentCuration(unittest.TestCase):

    def setUp(self):
        self.sources = ["https://news_source_1.com/rss", "https://news_source_2.com/rss"]
        self.criteria = {"freshness": 7, "relevance": 0.8, "topic": "AI"}

    def test_curate_content(self):
        curated_articles = curate_content(self.sources, self.criteria)
        
        # Check if the function returns a list
        self.assertIsInstance(curated_articles, list)
        
        # Check if the list is not empty
        self.assertTrue(len(curated_articles) > 0)
        
        # Check if each article in the list is a dictionary
        for article in curated_articles:
            self.assertIsInstance(article, dict)
            
            # Check if each article has the necessary keys
            self.assertTrue('title' in article)
            self.assertTrue('content' in article)
            self.assertTrue('link' in article)

if __name__ == '__main__':
    unittest.main()
```