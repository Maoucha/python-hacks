# import Lib for encryting strings
import hashlib

# Define functions
def encryptMD5(string):
	m = hashlib.md5()
	m.update(str(string).encode('utf-8'))
	return m.hexdigest()

print encryptMD5("bite")
