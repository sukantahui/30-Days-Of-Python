import mysql.connector as m
try:
    mycon=m.connect(
        host='localhost',
        user='root',
        password='sukantahui',
        database='office_db')
    if mycon.is_connected():
        print("MYSQL database is connected")
except:
    print("Unable to connect")    
    quit()
mycur=mycon.cursor()
mycur.execute("select * from states")
myresult=mycur.fetchall()
print("States are: ")
for row in myresult:
    print(row)