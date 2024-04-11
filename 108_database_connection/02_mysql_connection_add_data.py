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
name=input("Enter state name: ")
state_code=int(input("Enter state state code: "))
sql="""insert into states (id,state_name,state_code) 
    VALUES (NULL,%s,%s)"""
val=(name,state_code)
mycur.execute(sql,val)
mycon.commit()
print(mycur.rowcount, "record inserted.")
mycur.execute("select * from states")
print("States are: ")
for row in mycur:
    print(row)