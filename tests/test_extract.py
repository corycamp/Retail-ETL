# Test extract module
import pytest
from src.extract.users import fetch_users

def test_fetch_users():
    users = fetch_users()
    assert isinstance(users, dict)
