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
print("Select operation: delete, insert, query, update")
oper = input()
file = open("phone.csv", "r")
csv_reader = csv.reader(file)

list_csv = []
for row in csv_reader:
    
    list_csv.append(row)
if oper == 'delete':
    print("delete everything?")
    a = input()
    if a == 'yes':
        sql1 = '''DELETE FROM users'''
        cursor.execute(sql1)
    else:
        user = input('Enter user\'s one data, please\n')
        sql = f"""
            delete from users
            where first_name = '{user}'
            or last_name = '{user}'
            or phone_number = '{user}'
            or email = '{user}';
        """
        cursor.execute(sql)
if oper == 'insert':
    print("options: file / new user")
    a = input() 
    if a == 'file':
        for i in list_csv:
            cursor.execute("INSERT into users(first_name, last_name, phone_number, email) VALUES (%s, %s, %s, %s)", i)
    elif a == 'new user':
        print("write first name, last name, phone and email")
        s = input()
        s = s.split(", ")
        cursor.execute("INSERT into users(first_name, last_name, phone_number, email) VALUES (%s, %s, %s, %s)", s)
if oper == 'query':
    opt = input("show: all \ user\n")
    if opt == 'user':
        user = input('Enter user\'s one data, please\n')
        sql = f"""
            select *
            from users
            where first_name = '{user}'
            or last_name = '{user}'
            or phone_number = '{user}'
            or email = '{user}';
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) > 0:
            print(result)
        else:
            print('There is not such name, do you want to insert it to the database?')
            t = input()
            if t == 'yes':
                print("write first name, last name, phone and email")
                s = input()
                s = s.split(", ")
                cursor.execute("INSERT into users(first_name, last_name, phone_number, email) VALUES (%s, %s, %s, %s)", s)
                
    if opt == 'all':
        sql2 = f"""
            select *
            from users;
        """
        cursor.execute(sql2)
        print(cursor.fetchall())

if oper == 'update':
    print("What to do you want to update: first name \ last name \ phone \ email")
    option = input()
    if option == 'phone':
        user = input('Enter user\'s one data, please\n')
        phone = input("Enter new phone number\n")

        sql = f"""
            update users
            set phone_number = '{phone}'
            where first_name = '{user}'
            or last_name = '{user}'
            or phone_number = '{user}'
            or email = '{user}';
        """
        cursor.execute(sql)
    if option == 'first name':
        user = input('Enter user\'s one data, please\n')
        phone = input("Enter new first name\n")

        sql = f"""
            update users
            set first_name = '{phone}'
            where first_name = '{user}'
            or last_name = '{user}'
            or phone_number = '{user}'
            or email = '{user}'
        """
        cursor.execute(sql)
    if option == 'last name':
        user = input('Enter user\'s one data, please\n')
        phone = input("Enter new last name\n")

        sql = f"""
            update users
            set last_name = '{phone}'
            where first_name = '{user}'
            or last_name = '{user}'
            or phone_number = '{user}'
            or email = '{user}'
        """
        cursor.execute(sql)
    if option == 'email':
        user = input('Enter user\'s one data, please\n')
        phone = input("Enter new email\n")

        sql = f"""
            update users
            set email = '{phone}'
            where first_name = '{user}'
            or last_name = '{user}'
            or phone_number = '{user}'
            or email = '{user}'
        """
        cursor.execute(sql)
    print("Updated")


conn.close()