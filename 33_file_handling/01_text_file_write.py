# The __file__ special variable is an attribute of a Python module that contains 
# the path of the script or module from which it is accessed. 
# It is naturally set by the interpreter when a Python script is executed or imported.


import os
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","w")
<<<<<<< HEAD
f.write("A quick brown fox jumps over the lazy dog.")
f.write("Sachin\n")
f.write("Sourav\n")
f.write("Virat\n")
f.write("Dhoni\n")
f.write("Sunil\n")
=======
data=input("Say something here: ")
f.write(data)
>>>>>>> 5e82f9ae18cd1ee985890a08ddaaaeecdf3e25ff
print("File created")
f.close()
