r"""
This is script create a file
"""

import datetime

def create_file():
	"""This function creates empty file"""
	with open(filename, "a+") as file:
		file.write(string)


#filename = str(datetime.datetime.now())+".txt"

filename = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"))+".txt"
string = "whatsup"