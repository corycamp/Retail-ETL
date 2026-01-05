# Hard-fail validation rules
def assert_no_nulls(data, key):
    assert all(row.get(key) is not None for row in data), f"Nulls found in {key}"

def assert_unique(data, key):
    values = [row.get(key) for row in data]
    assert len(values) == len(set(values)), f"Duplicates found in {key}"
