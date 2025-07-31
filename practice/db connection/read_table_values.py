import pymysql

# establish the database connection
db = pymysql.connect("localhost", "root", "", "code_master" ) # (host,username,password,database_name)

# prepare a cursor object using database connection object and cursor() method
cur = db.cursor()

# defining table creation query
select_query = """SELECT * FROM student_details"""

try:
	cur.execute(select_query) # executes table creation query
	output = cur.fetchall() # returns all the row values
	
	for row in output:
		reg_no = row[0]
		f_name = row[1]
		l_name = row[2]
		age = row[3]
		sex = row[4]
		dept = row[5]
		percent = row[6]
		print ("Reg No :: %d , First Name :: %s , Last Name :: %s , Age :: %d , Sex :: %c , Department :: %s , Percentage :: %f" % (reg_no,f_name,l_name,age,sex,dept,percent))
		
except Exception as e:
	print ("Error :: " + str(e))
	
# disconnects the database connection
db.close()
