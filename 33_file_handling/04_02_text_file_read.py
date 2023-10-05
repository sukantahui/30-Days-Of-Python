import os
path=os.path.dirname(__file__)
print(path)
f=open(path+"\sukanta.txt","r")
print(f.read(11)) # WILL PRINT ABCDEFGHIJK
print(f.read(10)) # WILL PRINT LMNOPQRSTU
f.seek(0) # Sets file cursor to the beginning
print(f.read(11)) # ABCDEFGHIJK
f.close() 