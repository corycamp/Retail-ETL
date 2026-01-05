# Transform transactions data
def transform_transactions(raw_carts):
    # Example transformation
    return [cart for cart in raw_carts if cart.get('userId')]
