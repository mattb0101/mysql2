import os
import datetime
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
        names = ["Jim", "Bob"]
        # Prepare a string with the same number of placceholders
        format_strings = ','.join(['%s']*len(names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), names)
        connection.commit()
finally: 
#Close the connection regardless of whether success or not!
    connection.close()