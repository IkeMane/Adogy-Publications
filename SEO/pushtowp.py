import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("WORDPRESS_PASSWORD")


def post_article_to_wordpress(title, content, status, author_id, username, password, url):
    credentials = (username, password)
    headers = {'Content-Type': 'application/json'}
    data = {
        'title': title,
        'content': content,
        'status': status,
        'author': author_id
    }

    response = requests.post(f'{url}/wp-json/wp/v2/posts', headers=headers, auth=credentials, data=json.dumps(data))

    if response.status_code == 201:
        new_post_data = response.json()
        new_post_id = new_post_data['id']
        print(f"Article created successfully with ID: {new_post_id}")
        return new_post_id
    else:
        print(f"Failed to create article. Status code: {response.status_code}")
        return None



def update_yoast_seo(url, post_id, seo_title, seo_description, focus_keyphrase, username, password):
    api_endpoint = f"{url}/wp-json/custom-yoast-api/v1/update-meta/"
    data = {
        "post_id": post_id,
        "seo_title": seo_title,
        "seo_description": seo_description,
        "focus_keyphrase": focus_keyphrase  # Add focus keyphrase to the data
    }
    response = requests.post(api_endpoint, auth=(username, password), json=data)
    return response.text



def main():
    article_content = ''' '''  # Replace with your article content
    username = 'isaac@harmon-digital.com'
    password = password
    url = 'https://harmon-digital.com'
    article_title = 'Harmon Digital Test Article'
    status = 'draft'
    author_id = 183853251  # Replace with the ID of the author

    new_article_id = post_article_to_wordpress(article_title, article_content, status, author_id, username, password, url)

    post_id = new_article_id  # Replace with your post ID
    seo_title = 'TEST SEO Title - I LOVE GPT4'
    seo_description = 'New SEO Description- I LOVE GPT4'
    focus_keyphrase = 'I LOVE GPT4'

    response = update_yoast_seo(url, post_id, seo_title, seo_description, focus_keyphrase, username, password)
    print(response)





