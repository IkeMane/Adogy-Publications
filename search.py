import json
import requests
import os

def search_for_url(api_key, search_engine_id, query):
    """Perform a Google search and return the top result URL."""
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query
    }
    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()  # Raises a HTTPError if the HTTP request returned an unsuccessful status code
        result = response.json()
        return result["items"][0]["link"] if "items" in result else "No URL found"
    except requests.RequestException as e:
        return f"Error: {str(e)}"

def update_json_with_urls(file_path, api_key, search_engine_id):
    """Update the JSON data with URLs obtained from Google Search."""
    try:
        with open(file_path, 'r') as file:
            json_data = file.read()
        data = json.loads(json_data)
        # rest of your code to update data
        return json.dumps(data, indent=4)
    except FileNotFoundError:
        return "File not found."
    except json.JSONDecodeError:
        return "Invalid JSON format."

# Read JSON from file
with open('data.json', 'r') as file:
    json_data = file.read()


def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")
    # Update JSON
    updated_json = update_json_with_urls(json_data, api_key, search_engine_id)

    # Write updated JSON back to file
    with open('data.json', 'w') as file:
        file.write(updated_json)

    # Print updated JSON
    print(updated_json)

if __name__ == "__main__":
    main()