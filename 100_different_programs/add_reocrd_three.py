import json



def add_record(record,position=0):
    with open("new.txt", "r") as file:
        existing_data = file.readlines()
        # insert the new student record at the 2nd position
        if position==0:
           position=len(existing_data)
        existing_data.insert(position, json.dumps(student) + "\n")

        # write the modified data back to the file
    with open("new.txt", "w") as file:
        file.writelines(existing_data)




student={}

name = input("Enter student name: ")
regn = input("Enter Registration: ")
student['name']=name
student['regn']=regn

    
#here 1 is second position    
add_record(student,1)    
