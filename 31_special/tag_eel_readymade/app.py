import eel
import requests
import os
import json
from random import randint

  
eel.init("web")  
def create_text_file(data):
    f = open("tag.txt","w")
    f.write(data)
    f.close()
    
  
# Exposing the random_python function to javascript
@eel.expose    
def random_python():
    return randint(1,100)

# using the eel.expose command  
@eel.expose  
# defining the function for addition of two numbers  
def fetch_tag():  
    with open('project.json', 'r') as f:
        global project_data
        project_data = json.load(f)
    global current_tag
    current_tag = project_data['current_tag']      
    return current_tag 

@eel.expose  
# defining the function for addition of two numbers  
def update_ip(new_ip):  
    print("updating ip")
    with open('project.json', 'r') as f:
        data = json.load(f)   
    data['ip']=new_ip     
    with open("project.json", "w") as jsonFile:
        json.dump(data, jsonFile)   
    tag_value=new_ip    


@eel.expose
def fetchTagDetails(jobId):
    response = requests.get("http://%s/gold_old/gold_api/public/api/dev/tag/job/%s" % (tag_value,jobId))
    if response.status_code==200:
        jobDetails = response.json().get('data')
        # create_text_file("testing file")
    return jobDetails

@eel.expose
def runBatch():
    os.system('test.bat')

@eel.expose
def printTag(jobdata):
    #spliting serialize array to dictionary
    data = dict(x.split("=") for x in jobdata.split("&"))
    print(data)
    f = open("tag.txt","w")
    f.write("N")
    f.write("\n")
    f.write("R110,0")
    f.write("\n")
    f.write("q831")
    f.write("\n")
    f.write("S2")
    f.write("\n")
    f.write("D12")
    f.write("\n")
    f.write("OEb")
    f.write("\n")
    f.write("A395,85,2,1,1,1,N,")
    f.write('"'+data['cust_short_name']+'"')
    f.write("\n")
    f.write('A245,85,2,1,1,1,N,"Of"')
    f.write("\n")
    f.write("B405,70,2,1,2,1,33,N,")
    f.write('"'+data['tag_prefix']+data['tag']+'"')
    f.write("\n")
    f.write("A405,33,2,2,1,1,N,")
    f.write('"'+data['brand']+'"')
    f.write("\n")
    
    f.write("A245,33,2,2,1,1,N,")
    f.write('"'+data['tag_prefix']+data['tag']+'"')
    f.write("\n")
    
    f.write("A680,80,2,1,1,1,N,")
    f.write('"'+data['product_code']+'-')
    f.write(data['price_code']+'"')
    f.write("\n")
    
    f.write('A602,80,2,1,1,1,N,"Size:"')
    f.write("\n")
    
    f.write("A549,80,2,1,1,1,N,")
    f.write('"'+data['size']+'"')
    f.write("\n")
    
    f.write('A490,80,2,1,1,1,N,"Qty:"')
    f.write("\n")
    
    f.write("A450,80,2,1,1,1,N,")
    f.write('"'+data['pieces']+'"')
    f.write("\n")
    
    f.write('A680,60,2,1,1,1,N,"Gold Weight:"')
    f.write("\n")
    
    f.write("A550,60,2,1,1,1,N,")
    f.write('"'+data['gold_used']+'"')
    f.write("\n")
    
    f.write('A480,60,2,1,1,1,N,"HM"')
    f.write("\n")
    f.write('A680,40,2,1,1,1,N,"Gross Weight:"')
    f.write("\n")
    
    f.write("A540,40,2,1,1,1,N,")
    f.write('"'+data['gross_weight']+'"')
    f.write("\n")
    
    f.write("\n")
    f.write('A680,20,2,1,1,1,N,"Charge:"')
    f.write("\n")
    
    f.write("\n")
    f.write("A600,20,2,1,1,1,N,")
    f.write('"'+data['lc']+'"')
    f.write("\n")
    f.write('A555,20,2,1,1,1,N,"X"')
    f.write("\n")
    
    f.write('A535,20,2,1,1,1,N,')
    f.write('"'+data['pieces']+'"')
    f.write("\n")

    f.write('A515,20,2,1,1,1,N,"="')
    f.write("\n")
    
    f.write("A505,20,2,1,1,1,N,")
    f.write('"'+data['total_lc']+'"')
    f.write("\n")
    
    f.write("P1")
    f.write("\n")
    
    
    f.close()
    os.system('print_tag.bat')
    
    
    # print(data)




# for readymade
@eel.expose
def get_price_ploss(price_code):
    with open('project.json', 'r') as f:
        data = json.load(f)   
    price_list=data['price_list']  
    return price_list[price_code]

@eel.expose
def new_tag(tag_number):
    print(tag_number)
    with open('project.json', 'r') as f:
        data = json.load(f)
    current_tag= data['current_tag']   
    current_tag['tag_number']= tag_number+1   
    data['current_tag'] = current_tag
    with open("project.json", "w") as jsonFile:
        json.dump(data, jsonFile)   
    return data['current_tag']

@eel.expose
def increase_tag(tag_number):
    with open('project.json', 'r') as f:
        data = json.load(f)
    current_tag= data['current_tag']   
    current_tag['tag_number']= tag_number+1   
    data['current_tag'] = current_tag
    with open("project.json", "w") as jsonFile:
        json.dump(data, jsonFile)   
    return data['current_tag']    

    
# Start the index.html file
eel.start("index.html")





