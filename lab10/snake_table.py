import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "pp_db",
    user = "my_username",
    password = "my_password"
)
conn.autocommit = True
cursor = conn.cursor()

print("Welcome to the snake game! your username :")
user = input()
sql = f"""
            select score, level
            from snake
            where username = '{user}';
        """
cursor.execute(sql)
result = cursor.fetchall()
if len(result) > 0:

    level = int(result[0][1])
    score = int(result[0][0])
    print(f'Hello, {user}! Your last score was {score} and level {level}')
else:
    level = 0
    score = 0
    s = list()
    s.append(user)
    s.append(level)
    s.append(score)
    cursor.execute("INSERT into snake(username, score, level) VALUES (%s, %s, %s)", s)
    print(f'Hello, {user}! ')
