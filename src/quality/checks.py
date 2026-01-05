# Row counts, nulls, duplicates
def check_row_counts(data):
    return len(data)

def check_nulls(data, key):
    return sum(1 for row in data if row.get(key) is None)

def check_duplicates(data, key):
    seen = set()
    return sum(1 for row in data if row.get(key) in seen or seen.add(row.get(key)))
