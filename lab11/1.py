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
#file = open("phone.csv", "r")
#csv_reader = csv.reader(file)

#list_csv = []
#for row in csv_reader:
    
#    list_csv.append(row)
str = input("Enter word\n")
sql = f"""SELECT *
FROM
	users
WHERE
	email LIKE '%{str}%'
    or first_name LIKE '%{str}%'
    or last_name LIKE '%{str}%'
    or phone_number LIKE '%{str}%';
"""
cursor.execute(sql)
result = cursor.fetchall()
print(result)
cursor.close()