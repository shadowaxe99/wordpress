import unittest
from src.editing_reviewing import edit_and_review

class TestEditingReviewing(unittest.TestCase):

    def setUp(self):
        self.article = {
            'title': 'AI in Healthcare',
            'content': 'Artificial Intelligence is revolutionizing healthcare.',
            'link': 'https://example.com/ai-in-healthcare',
            'meta_description': 'This article discusses the impact of AI in healthcare.',
            'keywords': ['AI', 'healthcare']
        }

    def test_edit_and_review(self):
        edited_article = edit_and_review(self.article)
        self.assertIsNotNone(edited_article)
        self.assertIn('title', edited_article)
        self.assertIn('content', edited_article)
        self.assertIn('link', edited_article)
        self.assertIn('meta_description', edited_article)
        self.assertIn('keywords', edited_article)

if __name__ == '__main__':
    unittest.main()