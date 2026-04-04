import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    host="127.0.0.1",
    port="5432",
    password="123456"
)

cursor = conn.cursor()

cursor.execute("INSERT INTO people (name) VALUES (2, 'something')")
cursor.execute("INSERT INTO people (name) VALUES (1, 'name')")

conn.commit()
print("SALAMALEKUM")

cursor.close()
conn.close()