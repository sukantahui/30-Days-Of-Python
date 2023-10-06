# The __file__ special variable is an attribute of a Python module that contains 
# the path of the script or module from which it is accessed. 
# It is naturally set by the interpreter when a Python script is executed or imported.


import os
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","w")
data=input("Say something here: ")
f.write(data)
print("File created")
f.close()
