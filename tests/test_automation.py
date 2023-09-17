```python
import unittest
from src import automation

class TestAutomation(unittest.TestCase):

    def setUp(self):
        self.article = {
            'title': 'Test Article',
            'content': 'This is a test article.',
            'link': 'http://test.com',
            'meta_description': 'Test article for automation',
            'keywords': ['test', 'article', 'automation']
        }
        self.published_articles = []

    def test_automate_publishing(self):
        automation.automate_publishing(self.article)
        self.assertIn(self.article, self.published_articles)

    def test_set_publish_status(self):
        status = automation.set_publish_status(self.article, 'draft')
        self.assertEqual(status, 'draft')

    def test_share_on_social_media(self):
        result = automation.share_on_social_media(self.article)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```