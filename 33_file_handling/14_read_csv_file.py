import csv
import os
os.system('cls')
fields=[]
path=os.path.dirname(__file__)
try:
    file=open(path+'/employeesx.csv', 'r')
    print(file.read())
    csvreader = csv.reader(file)
    fields = next(csvreader)
    print(fields)
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
finally:    
    try:
        file.close()    
    except:
        print("Nothing to do")
