import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "my_database",
    user = "my_username",
    password = "my_password"
)

sql = 'select * from phonebook'

cursor = conn.cursor()
cursor.execute(sql)
phonebook = cursor.fetchall()

print(phonebook)
