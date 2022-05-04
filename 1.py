import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "pp_db",
    user = "my_username",
    password = "my_password"
)
conn.autocommit = True
with conn.cursor() as cursor:
    cursor.execute(
        """insert into users(first_name, last_name, phone_number, email)
                values('Madina', 'Leker','+767584378', 'madina@mail.com');
        """
    )

conn.close()