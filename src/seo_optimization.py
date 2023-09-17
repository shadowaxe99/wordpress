```python
from collections import defaultdict
from utils import extract_keywords, generate_meta_description

# Shared variables
curated_articles = []
meta_descriptions = defaultdict(str)
keywords = defaultdict(list)

def optimize_seo():
    """
    Function to generate meta descriptions and keywords for each curated article.
    """
    for article in curated_articles:
        # Generate meta description
        meta_descriptions[article.title] = generate_meta_description(article.content)

        # Generate keywords
        keywords[article.title] = extract_keywords(article.content)

    # Integrate the generated meta descriptions and keywords into the WordPress posts
    integrate_seo_to_wordpress()

def integrate_seo_to_wordpress():
    """
    Function to integrate the generated meta descriptions and keywords into the WordPress posts.
    """
    for article in curated_articles:
        # Get the meta description and keywords for the article
        meta_description = meta_descriptions[article.title]
        keyword_list = keywords[article.title]

        # Update the WordPress post with the meta description and keywords
        update_wordpress_post(article, meta_description, keyword_list)

def update_wordpress_post(article, meta_description, keyword_list):
    """
    Function to update a WordPress post with a given meta description and list of keywords.
    """
    # TODO: Implement the function to update the WordPress post with the meta description and keywords
    pass
```