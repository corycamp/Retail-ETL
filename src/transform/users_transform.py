# Transform users data
def transform_users(raw_users):
    # Example transformation
    return [user for user in raw_users if user.get('email')]
