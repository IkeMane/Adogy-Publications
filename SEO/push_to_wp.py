import requests
import json
from dotenv import load_dotenv
import os
import base64

load_dotenv()


def post_article_to_wordpress(title, content, status, author_id, username, password, url, featured_image_id):
    credentials = (username, password)
    headers = {'Content-Type': 'application/json'}
    data = {
        'title': title,
        'content': content,
        'status': status,
        'author': author_id,
        'featured_media': featured_image_id
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




def upload_image_to_wordpress(image_path, username, password, url):
    media_url = f'{url}/wp-json/wp/v2/media'
    headers = {
        'Content-Disposition': f'attachment; filename={image_path.split("/")[-1]}',
        'Authorization': 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()
    }
    with open(image_path, 'rb') as img:
        response = requests.post(media_url, headers=headers, files={'file': img}, auth=(username, password))

    if response.status_code == 201:
        return response.json()['id']
    else:
        print(f"Failed to upload image. Status code: {response.status_code}")
        return None




def update_yoast_seo(url, post_id, seo_title, seo_description, focus_keyphrase, username, password):
    api_endpoint = f"{url}/wp-json/custom-yoast-api/v1/update-meta/"
    data = {
        "post_id": post_id,
        "seo_title": seo_title,
        "seo_description": seo_description,
        "focus_keyphrase": focus_keyphrase # Add focus keyphrase to the data
    }
    response = requests.post(api_endpoint, auth=(username, password), json=data)
    return response.text



def push_to_wordpress(username, password, url, article_title, article_content, status, author_id , seo_title, seo_description, focus_keyphrase, image_path = 'image.jpg'):
    image_id = upload_image_to_wordpress(image_path, username, password, url)
    new_article_id = post_article_to_wordpress(article_title, article_content, status, author_id, username, password, url,image_id)
    post_id = new_article_id 
    response = update_yoast_seo(url, post_id, seo_title, seo_description, focus_keyphrase, username, password)
    print(response)




if __name__ == '__main__':
    username = os.getenv("WORDPRESS_USERNAME")
    password = os.getenv("WORDPRESS_PASSWORD")
    url = os.getenv("WORDPRESS_URL")
    article_content = ''' '''  # Replace with your article content
    article_title = 'Harmon Digital Test Article'
    status = 'draft'
    author_id = 183853251  
    seo_title = 'TEST SEO Title - I LOVE GPT4'
    seo_description = 'New SEO Description- I LOVE GPT4'
    focus_keyphrase = 'I LOVE GPT4'

    push_to_wordpress(username, password, url, article_title, article_content, status, author_id , seo_title, seo_description, focus_keyphrase)
