# Load dim_products
def load_products(session, products):
    session.bulk_insert_mappings(ProductTable, products)
    session.commit()
