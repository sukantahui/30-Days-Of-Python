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
sql="""insert into states (id,state_name,state_code) 
    VALUES (NULL,%s,%s)"""
val=[('Jammu & Kashmir',1),
('Himachal Pradesh',2),
('Punjab',3),
('Chandigarh',4),
('Uttranchal',5)]
mycur.executemany(sql,val)
mycon.commit()
print(mycur.rowcount, "record inserted.")
mycur.execute("select * from states")
print("States are: ")
for row in mycur:
    print(row)