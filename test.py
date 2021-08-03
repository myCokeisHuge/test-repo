import sqlite3

connection = sqlite3.connect('data.db') # coonnection string for SQL Lite DB

cursor = connection.cursor()  # cursor runs queries and stores result

# creates a DB
create_table = "CREATE TABLE users (id int, user text, password text)"
cursor.execute(create_table)

# Inserts a single user in DB
user = (1, "jose", 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# Inserts multiple users
users = [(2, "dicknose", 'asdf'),
         (3, "dickface", 'asdf'),
         (4, "mcjuggins", 'asdf')]
cursor.executemany(insert_query, users)

# select rows from DB and print them
user_list = []
select_query = "SELECT * FROM users"
for _id, name, pw in cursor.execute(select_query):
    user_list.append({'id': _id, 'user': name, 'pw': pw})

print(user_list)

connection.commit()
connection.close()
