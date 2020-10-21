import os
import pymysql

#Get username from GitHub workspace
username = os.getenv('gitpod')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a Query
    with connection.cursor() as cursor:
        SQL = "SELECT * FROM Artist;"
        cursor.execute(SQL)
        result = cursor.fetchall()
        print(result)
finally: 
#Close the connection regardless of whether success or not!
    connection.close()