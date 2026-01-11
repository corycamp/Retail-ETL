# API client + pagination
import requests
from src.config import API_BASE_URL

def get_paginated(endpoint, params=None):
    has_next_page = True
    batch = 30
    skip = 0
    data = []
    try:
        while has_next_page: 
            url = f"{API_BASE_URL}/{endpoint}?limit={batch}&skip={skip}"
            response = requests.get(url, params=params)
            response.raise_for_status()
            total = response.json()["total"]
            data = [*data, *response.json()[endpoint]]
            skip += batch
            has_next_page = skip < total
        return data
    except requests.RequestException as e:
        print(f"Error fetching data from {endpoint}: {e}")
        return None
