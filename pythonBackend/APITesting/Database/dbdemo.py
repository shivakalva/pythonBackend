import mysql.connector
#host, database, user, password
connection = mysql.connector.connect(host='localhost' ,database='APIDevelop', user='root',password='Root')
print(connection.is_connected())

cursor = connection.cursor()
cursor.execute('select * from CustomerInfo')