import mysql.connector
from mysql.connector import errorcode
try:
	banco_connection = mysql.connector.connect(host='localhost', user='root', password='', database='banco')
	print("Database connection made!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:
	banco_connection.close()

from mysql.connector import (connection)
banco_connection = connection.MySQLConnection(host='127.0.0.1', user='root', password='', database='banco')
banco_connection.close()