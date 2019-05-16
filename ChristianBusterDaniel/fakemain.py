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

while True:
    layout = [[sg.Text('Hvad vil du?')],
              [sg.Button("Nyt fravær"), sg.Button("Se fravær"),sg.Button('Exit')]]
    window = sg.Window('Fravær')
    event, values = window.Layout(layout).Read()

    if (event=="Nyt fravær"):
        window.Close()
        layout = [[sg.Text('Uge'), sg.InputText()],
                  [sg.Text('Dato'), sg.InputText()],
                  [sg.Text('Time'), sg.InputText()],
                  [sg.Text('Fravær'), sg.InputText()],
                  [sg.Button("Upload"),sg.Button("Back")]]
        window = sg.Window('Fravær')
        event, values = window.Layout(layout).Read()

        if (event!="Back"):
            for i in range(len(values)):
                values[i]=float(values[i])

            SaveToFile(values)
            data=ReadFromFile()
        window.Close()

    if (event=="Se fravær"):

        fravær = []
        uge = []

        samletFravær=0

        a = 0
        for rows in data:
            print(rows)
            fravær.append(data[a][0])
            uge.append(data[a][1])

            samletFravær=samletFravær+fravær[a]

            a = a + 1


        window.Close()
        layout = [[sg.Text("Alt fravær: "+str(int(samletFravær))+" sekunder")]]
        window = sg.Window('Fravær')
        event, values = window.Layout(layout).Read()

    if (event=="Exit"):
        exit()

