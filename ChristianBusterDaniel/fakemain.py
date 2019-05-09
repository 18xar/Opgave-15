#Vores fake main fil 1

import csv

#with open('data.csv', 'r') as readFile:
#    data = list(csv.reader(readFile))
#print(data)

#fravær=[]

def ReadFromFile():
    with open('data.csv', newline='') as csvfile:
        data = [list(map(int, rec)) for rec in csv.reader(csvfile, delimiter=',')]
        return data

        #print(data)
        #rows=0
        #for row in data:
        #    fravær.append(data[rows][1])
        #    rows = rows + 1


def SaveToFile(newData):
    with open('data.csv', 'a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(newData)

SaveToFile([1,3,128])
