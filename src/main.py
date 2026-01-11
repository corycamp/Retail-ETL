# Pipeline entry point
from sqlalchemy import text
from src.extract import carts, products, users
from datetime import datetime
import uuid
import json
from src.db.connection import SessionLocal


def raw_data_extraction():
    print("Extracting raw data from API...")
    uuid_value = uuid.uuid4()
    print(f"Generated UUID for extraction session: {uuid_value}")
    timestamp = datetime.now().isoformat() + "Z"
    try:
        [productData, cartData, userData] = [products.fetch_products(), carts.fetch_carts(), users.fetch_users()]
        print(f"Extracted {len(productData)} products.")
        print(f"Extracted {len(cartData)} carts.")
        print(f"Extracted {len(userData)} users.")
    except Exception as e:
        print(f"Error during data extraction: {e}")
        return
    
    raw_product_object = {
        "run_id": str(uuid_value),
        "ingested_at": timestamp,
        "data": json.dumps(productData)
    }
    raw_cart_object = {
        "run_id": str(uuid_value),
        "ingested_at": timestamp,
        "data": json.dumps(cartData)
    }
    raw_user_object = {
        "run_id": str(uuid_value),
        "ingested_at": timestamp,
        "data": json.dumps(userData)
    }
    
    print(f"Prepared raw product data with run_id: {raw_product_object['run_id']} and timestamp: {raw_product_object['ingested_at']}")
    print(f"Prepared raw cart data with run_id: {raw_cart_object['run_id']} and timestamp: {raw_cart_object['ingested_at']}")
    print(f"Prepared raw user data with run_id: {raw_user_object['run_id']} and timestamp: {raw_user_object['ingested_at']}")
    
    
    print("Loading raw data into storage...")
    with SessionLocal() as session:
        try:
            session.execute(text("INSERT INTO raw_products (p_id, run_id, ingested_at, payload) VALUES (:p_id, :run_id, :ingested_at, :payload)"),
                            {"p_id": str(uuid_value), "run_id": raw_product_object['run_id'], "ingested_at": raw_product_object['ingested_at'], "payload": raw_product_object['data']})
            session.execute(text("INSERT INTO raw_carts (c_id, run_id, ingested_at, payload) VALUES (:c_id, :run_id, :ingested_at, :payload)"),
                            {"c_id": str(uuid_value), "run_id": raw_cart_object['run_id'], "ingested_at": raw_cart_object['ingested_at'], "payload": raw_cart_object['data']})
            session.execute(text("INSERT INTO raw_users (u_id, run_id, ingested_at, payload) VALUES (:u_id, :run_id, :ingested_at, :payload)"),
                            {"u_id": str(uuid_value), "run_id": raw_user_object['run_id'], "ingested_at": raw_user_object['ingested_at'], "payload": raw_user_object['data']})
            session.commit()
            print("Raw data successfully loaded into storage.")
        except Exception as e:
            session.rollback()
            print(f"Error loading data into storage: {e}")
        
def main():
    print("Starting Retail ETL pipeline...")
    try:
        raw_data_extraction()
        print("Retail ETL pipeline completed.")
    except Exception as e:
        print(f"Error in ETL pipeline: {e}")
    

if __name__ == "__main__":
    main()
