import psycopg2

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="Din$$$05",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(50)
)
""")

conn.commit()
cur.close()
conn.close()

print("✅ Table created successfully!")