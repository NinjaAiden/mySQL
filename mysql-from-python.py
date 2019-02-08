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
        cursor.execute(""" CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime); """)
        # Note the above will still display a warning (not error) if the table
        # already exists
        
finally:
    # close connection, regardless of success status
    connection.close()