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

# number of lines in the file
index = 0

#read all the lines of the file one by one
while line != "":
	index += 1
	print str(index) + ": " + line[:-1]
	line = input_file.readline()



	
