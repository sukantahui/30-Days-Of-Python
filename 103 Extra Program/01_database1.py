import mysql.connector as m
myconnector = m.connect(host = "localhost",user= "root",password="sukantahui",database="exam_db")
if myconnector.is_connected():
    mycur=myconnector.cursor()
    mycur.execute("Select * from subjects where subject_short_name like 'MS-Excel%'")
    data=mycur.fetchall()
    # print(data)
    print("Here is your reversed list")
    for i in range(mycur.rowcount-1,-1,-1):
        print(data[i])
    
    
else:
    print("not found")
        