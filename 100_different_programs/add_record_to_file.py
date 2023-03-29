def add_student_record(position):
    # Ask the user for the student details
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    
    # Open the file in append mode
    with open("student_records.txt", "a") as file:
        # Write the student details to the file
        file.write(f"{name},{age},{grade}\n")
    
    print("Student record added successfully.")
    
    # Open the file for both reading and writing
    with open('student_records.txt', 'r+') as file:
        # Read the existing data into a list
        lines = file.readlines()

        # Create a new student record
        new_student = 'Jane Doe, 123456, Computer Science\n'

        # Insert the new student record at the 2nd position in the list
        # lines.insert(1, new_student)
        lines.insert(1, thisdict)

        # Move the file pointer to the beginning of the file
        file.seek(0)

        # Write the modified data back to the file
        file.writelines(lines)
    
    

add_student_record(2)
    