from Autoblog import autoblog, seo, generate_json, methodology
from photos import run_images
from push_to_wp import push_to_wordpress
from screenshot import screenshot
from dotenv import load_dotenv
import os

load_dotenv()

#wordpress
keyword = os.getenv("KEYWORD")
username = os.getenv("WORDPRESS_USERNAME")
password = os.getenv("WORDPRESS_PASSWORD")
url = os.getenv("WORDPRESS_URL")
author_id = os.getenv("WP_AUTHOR_ID")
status = os.getenv("WP_STATUS")

def write_to_file(filename,items):
    with open(filename, 'w') as file:
        file.write(items)

#TODO: gather the data based off keyword
#TODO: Sort data based off methodology

methodology_ = methodology(keyword)
items = generate_json(keyword, methodology_)
write_to_file('data.json',items)
screenshot()
article = autoblog(keyword,methodology_) #TODO: use assistants or files to add internal links.
run_images(keyword) #TODO: add a check to see if the image is already being used.
article_title, focus_keyphrase, meta_description, seo_title = seo(article)
push_to_wordpress(username, password, url, article_title, article, status, author_id, seo_title, meta_description, focus_keyphrase)