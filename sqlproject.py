'''
Database connectivity using python
'''
import mysql.connector
try:
    mydb=mysql.connector.connect(host="localhost",
                                 username="root",
                                 passwd="Kareem234",
                                 database="kareem",
                                 auth_plugin="mysql_native_password")
    cursor=mydb.cursor()

    q1="show databases"
    cursor.execute(q1)
    db=cursor.fetchall()
    if db:
        for i in db:
            print(i)


    if mydb.is_connected():
        print("Connected to the MYSQL database")
except mysql.connector.Error as err:
    print(f"Error {err}")
#pip install -U httpcore httpx
finally:
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("Connection closed")
