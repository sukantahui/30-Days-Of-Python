import os
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","r")
<<<<<<< HEAD
while True:
    line=f.readline()
    if not line:
        break
    print(line.strip())
=======
doc=f.read()
print(doc)
>>>>>>> 5e82f9ae18cd1ee985890a08ddaaaeecdf3e25ff
f.close()