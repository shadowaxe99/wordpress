```python
import os
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from src.utils import share_on_social_media

def automate_publishing(curated_articles, published_articles):
    wp_url = os.getenv("WP_URL")
    wp_username = os.getenv("WP_USERNAME")
    wp_password = os.getenv("WP_PASSWORD")

    wp = Client(wp_url, wp_username, wp_password)

    for article in curated_articles:
        post = WordPressPost()
        post.title = article.title
        post.content = article.content
        post.terms_names = {
            'post_tag': article.keywords,
            'category': ['News']
        }
        post.post_status = 'draft'  # set post to 'draft' for review

        post_id = wp.call(NewPost(post))
        article.id = post_id

        # Once reviewed and edited, publish the article
        if article in published_articles:
            post.post_status = 'publish'
            wp.call(NewPost(post))

            # Share the published articles on social media platforms
            share_on_social_media(article)

        print(f"Article '{article.title}' has been published with ID {post_id}")
```