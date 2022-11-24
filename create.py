import sqlite3
from faker import Faker

# connection = sqlite3.connect(':memory:')
connection = sqlite3.connect('sample.db')
cursor = connection.cursor()

table_drop = 'DROP TABLE IF EXISTS people' 
table_create = 'CREATE TABLE people (id INTEGER PRIMARY KEY, name TEXT, surname TEXT)'
cursor.execute(table_drop)
cursor.execute(table_create)
connection.commit()

fake = Faker()
names = [fake.name().split() for i in range(100)]
names = [n for n in names if len(n)==2]

insert_query = 'INSERT INTO people(name, surname) VALUES(?, ?)'
for n in names:
    cursor.execute(insert_query, n)
connection.commit()

select_query = 'SELECT * FROM people LIMIT 10'
for i in cursor.execute(select_query):
    print(i)

# in terminal: sqlite3 sample.db -> SELECT * FROM people LIMIT 10;