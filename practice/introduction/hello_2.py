import sys

def main(name):
	print ("Hello World " + name, end="\n")

# predefined main function
if __name__ == "__main__":
	main(sys.argv[1]) # 'sys.argv[]' used to get first command line arguments

print ("Welcome to Python")