# fetch_products()
from .dummyjson_client import get_paginated

def fetch_products():
    return get_paginated('products')
