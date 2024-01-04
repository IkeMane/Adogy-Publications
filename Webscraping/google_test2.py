from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

def fetch_all_search_results(search_query):
    """
    Fetches all the search results from Google using SerpApi.

    Args:
    search_query (str): The search term.

    Returns:
    str: All search results or an error message.
    """

    # SerpApi setup
    load_dotenv()
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return "SerpApi API key not found. Please set your API key."

    params = {
        "engine": "google",
        "q": search_query,
        "api_key": api_key
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        return results

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    search_query = "top publications"
    print(fetch_all_search_results(search_query))
