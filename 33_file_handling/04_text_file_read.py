# The __file__ special variable is an attribute of a Python module that contains 
# the path of the script or module from which it is accessed. 
# It is naturally set by the interpreter when a Python script is executed or imported.


import os
os.system('cls')
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","r")
x=f.read()
list=x.split()
print(list)
max=""

for i in list:
    if len(i)>len(max):
        max=i
print("The greatest word is ",max)
f.close()