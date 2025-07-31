import pymysql

# establish the database connection
db = pymysql.connect("localhost", "root", "", "code_master" ) # (host,username,password,database_name)

# prepare a cursor object using database connection object and cursor() method
cur = db.cursor()

# defining table creation query
update_query = "UPDATE student_details SET Age = '23' WHERE Reg_No = '3456'"

try:
	cur.execute(update_query) # executes table creation query
	db.commit()	# commit or save the changes
except Exception as e:
	print ("Error :: " + str(e))
	db.rollback() # rollbacks the activity
	
# disconnects the database connection
db.close()
