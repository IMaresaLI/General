import mysql.connector

connection = mysql.connector.connect(
     host='127.0.0.1',
     user='root',
     password='mysql',
     database='databaseprogram')
cursor = connection.cursor()