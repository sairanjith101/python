import pymysql

# establish the database connection
db = pymysql.connect("localhost", "root", "", "code_master" ) # (host,username,password,database_name)

# prepare a cursor object using database connection object and cursor() method
cur = db.cursor()

# defining table drop query
drop_query = 'DROP TABLE IF EXISTS student_details'

cur.execute(drop_query) # executes table drop query

# defining table creation query
create_query = """CREATE TABLE student_details (
	Reg_No INT(12) NOT NULL PRIMARY KEY,
	First_Name  VARCHAR(30) NOT NULL,
	Last_Name  CHAR(30),
	Age INT(2) NOT NULL,
	Sex CHAR(1) NOT NULL,
	Department VARCHAR(20) NOT NULL,
	Percentage FLOAT(5) NOT NULL )"""
	
cur.execute(create_query) # executes table creation query

# disconnects the database connection
db.close()
