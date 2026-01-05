# Load fact_transactions
def load_transactions(session, transactions):
    session.bulk_insert_mappings(TransactionTable, transactions)
    session.commit()
