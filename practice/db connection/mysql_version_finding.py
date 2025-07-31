import pymysql

# establish the database connection
db = pymysql.connect("localhost", "root", "", "code_master" ) # (host,username,password,database_name)

# prepare a cursor object using database connection object and cursor() method
cur = db.cursor()

# execute MySQL query using execute() method along with the cursor object.
cur.execute("SELECT VERSION()")

# fetchone() method or fetchall()[0] is used to fetch the single row.
data = cur.fetchone()
print ("Database version : %s" %data)

# disconnects the database connection
db.close()
