# Python program to implement the file concept using readlines ( ) for reading a file  
players = ["Sachin\n", "Sourav\n", "Sujit\n", "Kapil\n"]  
# writing to file  
file = open('hello.txt', 'w')  
file.writelines(players)                              # writelines is used to write the data into the file in                                                # the form of a list, by inserting multiple values at the same time,   
                                                       # here, we are taking the hello.txt file   
file.close()                                           # This instruction is used to close the file, i.e., hello.txt  
# Using readlines()  
file = open('hello.txt', 'r')  
Statements = file.readlines()  
count = 0  
# Strips the newline character  
for line in Statements:                                     # Using for loop to print the data of the file  
  count = count + 1  
  print("Statement{}: {}".format(count, line.strip()))  