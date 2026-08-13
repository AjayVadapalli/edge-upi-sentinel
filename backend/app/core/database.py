# import psycopg2
# from psycopg2.extras import RealDictCursor

import os
import psycopg2

# def get_connection():
#     conn = psycopg2.connect(
#         host="localhost",
#         database="edge_upi_risk",
#         user="postgres",
#         password="YOUR_PASSWORD"
#     )
#     return conn

def get_connection():
    return psycopg2.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432"),
        database=os.getenv("PGDATABASE", "edge_upi_risk"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.environ["PGPASSWORD"],
    )