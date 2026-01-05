# API client + pagination
import requests
from src.config import API_BASE_URL

def get_paginated(endpoint, params=None):
    url = f"{API_BASE_URL}/{endpoint}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
