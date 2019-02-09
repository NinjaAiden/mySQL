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
        list_of_names = ['fred', 'Fred']
        # prepare a string with the same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE fROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
        
finally:
    # close connection, regardless of success status
    connection.close()