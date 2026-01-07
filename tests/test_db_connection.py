# Test database connection using .env settings
from sqlalchemy import text
from src.db.connection import engine
from sqlalchemy.exc import OperationalError

def test_database_connection():
    try:
        with engine.connect() as conn:
            print("Database connection successful.")
            conn.execute(text("SELECT * FROM raw_products LIMIT 1;"))
            conn.execute(text("SELECT * FROM raw_users LIMIT 1;"))
            conn.execute(text("SELECT * FROM raw_carts LIMIT 1;"))
            print("Successfully queried raw tables.")
    except OperationalError as e:
        assert False, f"Database connection failed: {e}"
