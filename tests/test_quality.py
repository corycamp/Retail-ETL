# Test quality module
from src.quality.checks import check_row_counts, check_nulls

def test_check_row_counts():
    data = [1, 2, 3]
    assert check_row_counts(data) == 3

def test_check_nulls():
    data = [{'a': 1}, {'a': None}]
    assert check_nulls(data, 'a') == 1
