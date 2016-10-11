# import Lib for encryting strings
import hashlib

# Define functions
def encryptMD5(string):
	m = hashlib.md5()
	m.update(str(string).encode('utf-8'))
	return m.hexdigest()

# read an input file
input_file = open("test.csv", "r")	
line = input_file.readline()


#read all the lines of the file one by one and hash them
while line != "":
	print encryptMD5(line[:-1])
	line = input_file.readline()




	
