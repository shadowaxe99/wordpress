```python
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class UserInteraction:
    def __init__(self):
        self.user_comments = []
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

    def analyze_comment(self, comment):
        sentiment_score = self.sentiment_analyzer.polarity_scores(comment)
        if sentiment_score['compound'] >= 0.05:
            return 'positive'
        elif sentiment_score['compound'] <= -0.05:
            return 'negative'
        else:
            return 'neutral'

    def respond_to_comment(self, comment):
        sentiment = self.analyze_comment(comment)
        if sentiment == 'positive':
            return 'Thank you for your positive feedback!'
        elif sentiment == 'negative':
            return 'We are sorry to hear that. We will strive to do better.'
        else:
            return 'Thank you for your feedback.'

    def interact_with_user(self, comment):
        response = self.respond_to_comment(comment)
        self.user_comments.append({'comment': comment, 'response': response})
        return response
```