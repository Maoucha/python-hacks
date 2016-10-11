# import Lib for encryting strings
import hashlib
import sys

# Define functions
def encryptMD5(string):
	m = hashlib.md5()
	m.update(str(string).encode('utf-8'))
	return m.hexdigest()

# read an input file
input_file = open(sys.argv[1], "r")
ouput_file = open("output.csv", "w")
line = input_file.readline()

#read all the lines of the file one by one and hash them
while line != "":
	ouput_file.write(encryptMD5(line[:-1]) + "\n")
	line = input_file.readline()
