# Insert JSON into raw tables
def load_raw_data(session, table, data):
    session.bulk_insert_mappings(table, data)
    session.commit()
