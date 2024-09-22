import os
import psycopg2
from psycopg2 import sql

# Database connection parameters (these will come from Railway's environment)
DB_HOST = os.getenv('PGHOST', 'localhost')
DB_NAME = os.getenv('PGDATABASE', 'postgres')
DB_USER = os.getenv('PGUSER', 'postgres')
DB_PASSWORD = os.getenv('PGPASSWORD', 'password')
DB_PORT = os.getenv('PGPORT', '5432')

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        print("Connected to the database")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_table(conn):
    try:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            age INT
        );''')
        conn.commit()
        print("Table created")
    except Exception as e:
        print(f"Error creating table: {e}")

def insert_data(conn, name, age):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO test_table (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
        print("Data inserted")
    except Exception as e:
        print(f"Error inserting data: {e}")

if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        create_table(conn)
        insert_data(conn, 'John Doe', 30)
        conn.close()
