import pymysql

# establish the database connection
db = pymysql.connect("localhost", "root", "", "code_master" ) # (host,username,password,database_name)

# prepare a cursor object using database connection object and cursor() method
cur = db.cursor()

# defining table creation query
insert_query = """INSERT INTO student_details 
	(Reg_No, First_Name, Last_Name, Age, Sex, Department, Percentage)
	VALUES ('3456','Devid','Mazeeta','23','M','MBA','70.0')"""

try:
	cur.execute(insert_query) # executes table creation query
	db.commit()	# commit or save the changes
except Exception as e:
	print ("Error :: " + str(e))
	db.rollback() # rollbacks the activity
	
# disconnects the database connection
db.close()
