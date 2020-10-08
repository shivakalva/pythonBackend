import mysql.connector
from utilties.configuration import *


#connection = mysql.connector.connect(host='localhost' ,database='APIDevelop', user='root',password='Root')

connection = getconnection()
cursor = connection.cursor()
query = "delete from customerinfo where CourseName = selenium"
#data = ("selenium")
cursor.execute(query)
connection.close()