from serpapi import GoogleSearch
import requests
import json
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("SERPAPI_API_KEY")

def get_lat_long(location_name):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(location_name)

    if location:
        return f"@{location.latitude},{location.longitude},14z"
    else:
        return "Location not found"

# Example usage
location_name = "St. Louis"
print(get_lat_long(location_name))


def search_google_maps(keyword, location):
    api_key = os.getenv("SERPAPI_API_KEY")
    ll = get_lat_long(location)
    params = {
        "engine": "google_maps",
        "q": keyword,
        "ll": ll, 
        "google_domain": "google.com",
        "api_key": api_key
    }

    response = requests.get("https://serpapi.com/search.json", params=params)
    data = response.json()

    results = []
    if "local_results" in data:
        for item in data["local_results"]:
            data_id = item.get("data_id", "")

            params = {
                "engine": "google_maps_photos",
                "data_id": data_id,
                "api_key": api_key
                }

            search = GoogleSearch(params)
            imageresults = search.get_dict()
            photos = imageresults.get("photos", [])
            if photos:
                # Get the first image's URL
                image_url = photos[0].get("image", "")
                print(image_url)

                result = {
                    "URL": item.get("website", ""),
                    "Image URL": image_url,
                    "Title": item.get("title", ""),
                    "Rating": item.get("rating", ""),
                    "Reviews": item.get("reviews", ""),
                    "Description": item.get("description", ""),
                }
                results.append(result)

    return json.dumps({"publications": results}, indent=4)

# Example usage
keyword = "Breakfast" #note this will not work yet- we need to add cordanates finder
location = "St. Louis"
print(search_google_maps(keyword, location))
