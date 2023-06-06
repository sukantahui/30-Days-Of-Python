# file=open("abc.txt",'w')
# file.write('There was a brown crow\n')
# file.write('Mounita is porom bandori\n')
# file.write('She is my enemy\n')
# file.write('I am Poromsundori\n')
# print(file)
# file.close()
file=open("abc.txt",'r')
# x=file.read()
# print(x)
# while True:
#     line=file.readline()
#     if not line:
#         break
#     print(line.strip())  
lines=file.readlines()
# print(lines)
print(lines[-1].strip())
file.close()