from cgi import print_directory
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
str = input("Please insert first name or phone number\n")
str = str.split(", ")
sql = f"""SELECT *
FROM
	users
WHERE
    first_name LIKE '{str[0]}'
    or phone_number LIKE '{str[0]}';
"""
cursor.execute(sql)
res = cursor.fetchall()
#print(res)
sql1 = f"""create or replace procedure deleteUser(first_name varchar, phone_number varchar)
as
$$
begin
    delete
    from users s
    where s.first_name = $1
    or s.phone_number = $2;
end;
$$
    LANGUAGE plpgsql;

call deleteUser('{res[0][0]}', '{res[0][2]}');"""
cursor.execute(sql1)
cursor.close()