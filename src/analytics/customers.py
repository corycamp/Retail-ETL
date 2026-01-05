# Load dim_customers
def load_customers(session, customers):
    # Example loader
    session.bulk_insert_mappings(CustomerTable, customers)
    session.commit()
