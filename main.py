from Autoblog import autoblog, seo
from photos import run_images
from SEO.push_to_wp import push_to_wordpress
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


#TODO: gather the data based off keyword
#TODO: Sort data based off methodology
article = autoblog(keyword) #TODO: use assistants or files to add internal links.
run_images(keyword) #TODO: add a check to see if the image is already being used.
article_title, focus_keyphrase, meta_description, seo_title = seo(article)
push_to_wordpress(username, password, url, article_title, article, status, author_id, seo_title, meta_description, focus_keyphrase)