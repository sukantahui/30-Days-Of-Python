import csv
import os
os.system('cls')
path=os.path.dirname(__file__)
file=open(path+'/employees.csv', 'w', newline='')
writer=csv.writer(file);
writer.writerow(['name','age', 'salary'])
writer.writerow(['Sunil Sen',36, 20000])
writer.writerow(['Amit Dutta',48, 19000])
writer.writerow(['Sumita Manna',22, 10000])

file.close()