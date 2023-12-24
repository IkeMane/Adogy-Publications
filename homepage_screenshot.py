import asyncio
import json
import random
import time
from pyppeteer import launch
import requests
import base64
from dotenv import load_dotenv
import os

load_dotenv()



wp_url = 'https://harmon-digital.com'
username = 'isaacdouglasharmon@gmail.com'
app_password = os.getenv("WP_APP_PASSWORD")

async def upload_to_wordpress(file_name):
    media_url = f'{wp_url}/wp-json/wp/v2/media'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f'{username}:{app_password}'.encode()).decode(),
        'Content-Disposition': f'attachment; filename={file_name}',
        'Content-Type': 'image/png',
    }
    try:
        with open(file_name, 'rb') as img:
            response = requests.post(media_url, headers=headers, data=img)
            if response.status_code == 201:
                return response.json()['source_url']
            else:
                print(f"Error uploading to WordPress: {response.json()}")
    except Exception as e:
        print(f"Exception during upload: {e}")
    return None




user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/74.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"
]


async def take_screenshot(url, filename, user_agent):
    try:
        browser = await launch()
        page = await browser.newPage()
        await page.setUserAgent(user_agent)
        await page.goto(url)
        await page.setViewport({'width': 1920, 'height': 1080})
        await page.waitFor(5000)  # Wait for 5 seconds
        await page.screenshot({'path': filename})
        await browser.close()
    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")

async def process_publications(file_path):
    # Load the JSON data from file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Process each publication
    for publication in data['publications']:
        if publication['URL'] != "URL not found":  # Check if URL is valid
            url = publication['URL']
            filename = f"screenshot_{publication['Title'].replace(' ', '_')}.png"
            user_agent = random.choice(user_agents)
            await take_screenshot(url, filename, user_agent)
            publication['Image URL'] = filename
            time.sleep(random.randint(10, 30))  # Random delay between 10 to 30 seconds

    # Write the updated JSON back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Path to the JSON file
file_path = 'publications.json'

# Run the process
asyncio.get_event_loop().run_until_complete(process_publications(file_path))
