import mysql.connector
from utilties.configuration import *

#host, database, user, password
#connection = mysql.connector.connect(host='localhost' ,database='APIDevelop', user='root',password='Root')
#print(connection.is_connected())
#Cursor object instantiate connection and allow to execute SQL query.

connection = getconnection()
cursor = connection.cursor()
cursor.execute('select * from customerinfo')
rows = cursor.fetchall()
#print(type(rows))
#print(rows)

##################getting the sum of the data retrived from the columns ##############################

sum = 0
for row in rows:
    sum = sum + row[2]
print(sum)

##################getting the data at run time ##############################

# query = "update customerInfo set Location = %s where CourseName = %s"
# data = ("UK", "Jmeter")
# cursor.execute(query,data)
cursor.execute('select * from customerinfo')
rows = cursor.fetchall()
print(rows)
connection.commit()
connection.close()