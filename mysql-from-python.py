import os
import datetime
import pymysql

# get username from cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # run a query on database
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends values (%s, %s, %s);", row)
        connection.commit()
        
finally:
    # close connection, regardless of success status
    connection.close()