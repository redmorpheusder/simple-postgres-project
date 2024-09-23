import os
import psycopg2
from psycopg2 import sql
from fastapi import FastAPI

app = FastAPI()

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

@app.post("/create_table")
def create_table():
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS test_table (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                age INT
            );''')
            conn.commit()
            print("Table created")
            return {"message": "Table created successfully"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            conn.close()

@app.post("/insert_data/")
def insert_data(name: str, age: int):
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO test_table (name, age) VALUES (%s, %s)", (name, age))
            conn.commit()
            print("Data inserted")
            return {"message": "Data inserted successfully"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            conn.close()


# New GET endpoint to fetch all data from test_table
@app.get("/get_data/")
def get_data():
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM test_table;")
            rows = cur.fetchall()
            result = []
            for row in rows:
                result.append({
                    "id": row[0],
                    "name": row[1],
                    "age": row[2]
                })
            return {"data": result}
        except Exception as e:
            return {"error": str(e)}
        finally:
            conn.close()


@app.get("/")
def root():
    return {"message": "Welcome to the PostgreSQL FastAPI app!"}
