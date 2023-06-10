# The __file__ special variable is an attribute of a Python module that contains 
# the path of the script or module from which it is accessed. 
# It is naturally set by the interpreter when a Python script is executed or imported.


import os
os.system('cls')
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","w")
f.write("A quick brown fox jumps over the lazy dog.\n")
f.write("The key function for working with files in Python is the open() function.\n")
f.write("r - Read - Default value. Opens a file for reading, error if the file does not exist.\n")
f.write("a- Append - Opens a file for appending, creates the file if it does not exist.\n")
f.write("w - Write - Opens a file for writing, creates the file if it does not exist.\n")
f.write("x- Create - Creates the specified file, returns an error if the file exists.\n")
f.write("t - Text - Default value. Text mode.\n")
f.write("b - Binary - Binary mode (e.g. images).\n")
f.close()
