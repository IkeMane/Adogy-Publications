from Autoblog import autoblog, seo, generate_json, methodology
from photos import run_images
from push_to_wp import push_to_wordpress
from screenshot import screenshot
from search import update_json_with_urls
from update_sheet import update_sheet
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

#wordpress
keyword = os.getenv("KEYWORD")
username = os.getenv("WORDPRESS_USERNAME")
password = os.getenv("WORDPRESS_PASSWORD")
url = os.getenv("WORDPRESS_URL")
author_id = os.getenv("WP_AUTHOR_ID")
status = os.getenv("WP_STATUS")
google_api_key = os.getenv("GOOGLE_API_KEY")
search_engine_id = os.getenv("SEARCH_ENGINE_ID")
sheet_id = os.getenv("SHEET_ID")
sheet_column_letter = os.getenv("SHEET_COLUMN_LETTER")
workbook = os.getenv("WORKBOOK")

def write_to_file(filename,items):
    with open(filename, 'w') as file:
        file.write(items)

#TODO: gather the data based off keyword
#TODO: Sort data based off methodology

methodology_ = methodology(keyword)
items = generate_json(keyword, methodology_)
write_to_file('data.json',items)
updated_json = update_json_with_urls('data.json',google_api_key, search_engine_id)
write_to_file('data.json',updated_json)
asyncio.run(screenshot())
article = autoblog(keyword,methodology_) #TODO: use assistants or files to add internal links.
run_images(keyword) #TODO: add a check to see if the image is already being used.
article_title, focus_keyphrase, meta_description, seo_title = seo(article)
permalink = push_to_wordpress(username, password, url, article_title, article, status, author_id, seo_title, meta_description, focus_keyphrase)
update_sheet(permalink, sheet_id, 'google_sheets_api.json',workbook, sheet_column_letter)