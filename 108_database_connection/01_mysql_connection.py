import mysql.connector as m
try:
    mycon=m.connect(
        host='localhost',
        user='root',
        password='sukantahui',
        database='office_db')
    if mycon.is_connected():
        print("MYSQL is connected")
except:
    print("Unable to connect")    
    quit()
mycur=mycon.cursor()
sql="""CREATE TABLE states (
    id bigint(20)  PRIMARY KEY AUTO_INCREMENT,
    state_name varchar(255) NOT NULL,
    state_code int(11) NOT NULL)"""
mycur.execute(sql)
mycur.execute("show tables")
# # myData=mycur.fetchall()
# # print(myData)
# # for row in myData:
# #     print(row[0])
print("Tables are: ")
for row in mycur:
    print(row[0])