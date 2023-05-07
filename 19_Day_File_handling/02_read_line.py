# Python program to implement the file concept using readline() for reading a file  
players=["Sachin\n", "Sourav\n", "Sujit\n", "Kapil\n"]
# Writing to a file  
file1 = open('new.txt', 'w')  
file1.writelines((players))                          # writelines is used to write the data into the file in                                                # the form of list, by inserting multiple values at a same time,   
                                                       # here we are taking new.txt file   
                                                         
file1.close()                                       # This instruction is used to close the file, i.e., hello.txt  
                                                                                
# Using readline()  
file1 = open('new.txt', 'r')  
count = 0  
while True:  
  count = count + 1  
  # Get next line from file  
  s = file1.readline()  
  
  # if line is empty  
  # end of file is reached  
  if not s:  
    break  
  print("Statement{}: {}".format(count, s.strip()))  
file1.close()  