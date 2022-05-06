import psycopg2
import csv
conn = psycopg2.connect(
    host = "localhost",
    database = "pp_db",
    user = "my_username",
    password = "my_password"
)
conn.autocommit = True
cursor = conn.cursor()
str = input("Please insert the data of the user\n")
str = str.split(", ")
sql = f"""SELECT *
FROM
	users
WHERE
    first_name LIKE '{str[0]}'
    and last_name LIKE '{str[1]}';
"""
cursor.execute(sql)
result = cursor.fetchall()

if len(result) > 0:
    sql2 = f"""create or replace procedure updateStudent(_first_name varchar, last_name varchar, _phone_number varchar, email varchar)
        as
        $$
        begin
            update users
            set phone_number = $3
            where first_name = $1;
        end;
        $$
            LANGUAGE plpgsql;

        call updateStudent('{str[0]}', '{str[1]}', '{str[2]}', '{str[3]}');"""
    cursor.execute(sql2)
  
else:
    sql1 = f"""create or replace procedure addUser(first_name varchar, last_name varchar, phone_number varchar, email varchar)
        as
        $$
        begin
            insert into users(first_name, last_name, phone_number, email) values ($1, $2, $3, $4);
        end;
        $$
            LANGUAGE plpgsql;

        call addUser('{str[0]}', '{str[1]}', '{str[2]}', '{str[3]}');"""
    cursor.execute(sql1)
  

cursor.close()