#Vores fake main fil 1

import csv

#with open('data.csv', 'r') as readFile:
#    data = list(csv.reader(readFile))
#print(data)

#fravær=[]

def ReadFromFile():
    with open('data.csv', newline='') as csvfile:
        data = [list(map(int, rec)) for rec in csv.reader(csvfile, delimiter=',')]
        print(data)
        return data

def SaveToFile(newData):
    with open('data.csv', 'a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(newData)

SaveToFile([2,3,128])

data=ReadFromFile()


fravær=[]
uge=[]

a=0
for rows in data:

    fravær.append(data[a][0])
    uge.append(data[a][1])

    a=a+1



