# Test transform module
from src.transform.users_transform import transform_users

def test_transform_users():
    raw = [{'email': 'a@b.com'}, {'email': None}]
    result = transform_users(raw)
    assert all(u['email'] for u in result)
