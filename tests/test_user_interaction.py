```python
import unittest
from src.user_interaction import interact_with_user

class TestUserInteraction(unittest.TestCase):

    def setUp(self):
        self.user_comments = [
            {"user_id": 1, "comment_text": "Great article!", "sentiment": "positive"},
            {"user_id": 2, "comment_text": "This is not very informative.", "sentiment": "negative"},
            {"user_id": 3, "comment_text": "I don't have an opinion on this.", "sentiment": "neutral"}
        ]

    def test_interact_with_user(self):
        for comment in self.user_comments:
            response = interact_with_user(comment)
            if comment["sentiment"] == "positive":
                self.assertIn("Thank you", response)
            elif comment["sentiment"] == "negative":
                self.assertIn("We're sorry", response)
            elif comment["sentiment"] == "neutral":
                self.assertIn("We appreciate", response)

if __name__ == '__main__':
    unittest.main()
```