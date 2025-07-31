import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='code_master',
    cursorclass=pymysql.cursors.DictCursor
)

with connection:
    with connection.cursor() as cursor:

        cursor.execute("SELECT VERSION()")

        version = cursor.fetchone()
        print("Database version : %s" %version)