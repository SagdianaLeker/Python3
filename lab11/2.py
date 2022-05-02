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
sql = f"""create or replace function getUser(first_name varchar)
    returns table
            (
                first_name varchar,
                last_name varchar
            )
as
$$
begin
    return query
       select s.first_name, s.last_name
       from users as s
       where s.first_name = $1;
end
$$ language plpgsql;

select *
from getUser('{str[0]}');"""
cursor.execute(sql);
result = cursor.fetchall()
#if len(result) > 0:
#    sql1 = f"""create or replace procedure addUser(first_name varchar, last_name varchar, phone_number varchar, email varchar)
#        as
#        $$
#        begin
#            insert into users(first_name, last_name, phone_number, email) values ($1, $2, $3, $4);
#        end;
#        $$
#            LANGUAGE plpgsql;
#
#        call addUser('{str[0]}', '{str[1]}', '{str[2]}', '{str[3]}');"""

#    cursor.execute(sql1)
cursor.close()