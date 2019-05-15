#Vores fake main fil 1

import csv,PySimpleGUI as sg

def ReadFromFile():
    with open('data.csv', newline='') as csvfile:
        data = [list(map(float, rec)) for rec in csv.reader(csvfile, delimiter=',')]
        print(data)
        return data

def SaveToFile(newData):
    with open('data.csv', 'a',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(newData)

data=ReadFromFile()

fravær=[]
uge=[]

a=0
for rows in data:
    fravær.append(data[a][0])
    uge.append(data[a][1])
    a=a+1

while True:
    layout = [[sg.Text('Hvad vil du?')],
              [sg.Button("Nyt fravær"), sg.Button("Se fravær"),sg.Button('Exit')]]
    window = sg.Window('Fravær')
    event, values = window.Layout(layout).Read()

    if (event=="Nyt fravær"):
        window.Close()
        layout = [[sg.Text('Uge'), sg.InputText()],
                  [sg.Text('Dato'), sg.InputText()],
                  [sg.Text('Fravær'), sg.InputText()],
                  [sg.Button("Upload")]]
        window = sg.Window('Fravær')
        event, values = window.Layout(layout).Read()

        for i in range(len(values)):
            values[i]=float(values[i])

        SaveToFile(values)
        data=ReadFromFile()
        window.Close()

    if (event=="Se fravær"):
        window.Close()

    if (event=="Exit"):
        exit()

        print(data)







    #print("")
    #print("Se fravær        1)")
    #print("Upload fravær    2)")
    #x=int(input(": "))

    #if (x==2):
    #    a=int(input("Uge: "))
    #    b=int(input("Fravær: "))

       # SaveToFile([a,b])


