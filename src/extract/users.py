# fetch_users()
from .dummyjson_client import get_paginated

def fetch_users():
    return get_paginated('users')
