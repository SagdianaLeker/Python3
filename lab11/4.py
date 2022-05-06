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
n = int(input())
sql = f"""CREATE OR REPLACE FUNCTION get_phonebook_option(n integer)
        RETURNS TABLE(_name VARCHAR, _phone VARCHAR) 
        AS
        $$
        BEGIN
            RETURN QUERY
	        SELECT name, phone
		    FROM phone
		    ORDER BY name
		    LIMIT n OFFSET 3;
        END;
        $$
        LANGUAGE plpgsql;
        SELECT *
        FROM get_phonebook_option({n})
        """
cursor.execute(sql)
print(cursor.fetchall())