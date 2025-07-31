import pymysql

# establish the database connection
db = pymysql.connect("localhost", "root", "", "code_master" ) # (host,username,password,database_name)

# prepare a cursor object using database connection object and cursor() method
cur = db.cursor()

# defining table creation query
delete_query = "DELETE FROM `student_details` WHERE Age = '23'"

try:
	cur.execute(delete_query) # executes table creation query
	db.commit()	# commit or save the changes
except Exception as e:
	print ("Error :: " + str(e))
	db.rollback() # rollbacks the activity
	
# disconnects the database connection
db.close()
