#count total number of word, space and vowel
import os
os.system('cls')
path=os.path.dirname(__file__)

print(path)
f=open(path+"/"+"test.txt","wb")
x="A quick brown fox"
f.write(x.encode())
f.close()
