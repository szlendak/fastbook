import os

import dotenv
import requests

dotenv.load_dotenv(".env")


def search_images_brave(term, max_images=100):
    url = "https://api.search.brave.com/res/v1/images/search"
    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip",
        "x-subscription-token": os.getenv("BRAVE_SEARCH_API_KEY"),
    }
    params = {"q": term, "count": max_images}

    response = requests.get(url, headers=headers, params=params)
    response_json = response.json()

    return response_json
