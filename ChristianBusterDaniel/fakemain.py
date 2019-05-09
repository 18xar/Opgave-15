#Vores fake main fil 1

import csv

def ReadFromFile():
    with open('data.csv', newline='') as csvfile:
        data = [list(map(int, rec)) for rec in csv.reader(csvfile, delimiter=',')]
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

while True:
    print("")
    print("Se fravær        1)")
    print("Upload fravær    2)")
    x=int(input(": "))

    if (x==2):
        print("hi")
        uge=float(input("Uge: "))
        fravær=float(input("Fravær: "))

        SaveToFile([uge,fravær])


