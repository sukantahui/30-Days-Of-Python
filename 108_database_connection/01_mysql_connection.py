import mysql. connector as m
mycon=m.connect(host='localhost',user='root',password='sukantahui',database='ses_gold')
if mycon.is_connected():
    print("Database is connected")
mycur=mycon.cursor()
mycur.execute('select * from job_master')
myData=mycur.fetchall()
for row in myData:
    print(row[0])