
handle = open('/home/vasya/Документы/Github/prog3/lab11/MOCKDATA.json')


print(handle)


lines = handle.readlines()


for line in lines:
    pass
id_list = []
what = "gender"
for line in lines:

   
    if line.find(what):
        temp2 = line.find(what)+len(what)+2
        temp = line.find(",",temp2,len(line)-1)
        ss = line[temp2:temp]
        ss2 = ss.replace("\"","")
        id_list.append({what:ss2})

handle.close()


import csv
import json

with open('MOCKDATA.json') as f:
    data_dict = json.load(f)
print(data_dict[0]['first_name'])
print(data_dict[0].values())

with open('eggs.csv', 'w', newline='') as csvfile:
    jsonwriter = csv.writer(
        csvfile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    jsonwriter.writerow(data_dict[0].keys())
    keys = data_dict[0].keys()
    for el in data_dict:
        jsonwriter.writerow(el.values())

