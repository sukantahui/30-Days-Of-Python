# The __file__ special variable is an attribute of a Python module that contains 
# the path of the script or module from which it is accessed. 
# It is naturally set by the interpreter when a Python script is executed or imported.


import os
os.system('cls')
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","w")
f.write("A quick brown fox jumps over the lazy dog.")
f.close()
