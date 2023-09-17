```python
import requests
from bs4 import BeautifulSoup

curated_articles = []

class Article:
    def __init__(self, title, content, link):
        self.title = title
        self.content = content
        self.link = link

def curate_content():
    sources = ["https://news_source_1.com/rss", "https://news_source_2.com/rss"]
    for source in sources:
        response = requests.get(source)
        soup = BeautifulSoup(response.content, features="xml")
        articles = soup.findAll('item')
        for a in articles:
            title = a.title.text
            content = a.description.text
            link = a.link.text
            article = Article(title, content, link)
            curated_articles.append(article)

curate_content()
```