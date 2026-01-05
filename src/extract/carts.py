# fetch_carts()
from .dummyjson_client import get_paginated

def fetch_carts():
    return get_paginated('carts')
