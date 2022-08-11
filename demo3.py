import psycopg2

connection = psycopg2.connect('dbname=mydb')

cursor = connection.cursor()

cursor.execute('SELECT * from table2;')
result = cursor.fetchall()
print(result)

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s,%s);', (3,True))

cursor.execute('SELECT * from table2;')

result2 = cursor.fetchone()
print('fetchone ' , result2)

result = cursor.fetchmany(2)
print('fetchmany ' , result2)

result3 = cursor.fetchone()
print('fetchone ' , result3)

connection.commit()

connection.close()
cursor.close()