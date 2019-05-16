#Vores fake main fil 1

import csv,PySimpleGUI as sg, math


def FraværGennemsnit (uge, fravær):
    #Hej123
    antaluge = len(uge)
    fraværialt = sum(fravær)
    gennemsnit = fraværialt/antaluge

    return(gennemsnit)

def mistetLøn(værdier, timeløn):

    mistetløn = værdier*timeløn

    return(mistetløn)

def graf(fravær,uger):
    graph.DrawLine((-100,-100), (100,-100))
    graph.DrawLine((-100,-100), (-100,100))

    for x in range(-100, 101, 20):
        graph.DrawLine((x,-103), (x,-97))

    for y in range(-100, 101, 20):
        graph.DrawLine((-103,y), (-97,y))

    for i in range(0,200,20):
        if y != 0:
            graph.DrawText( i, (-100,i+10-100), color='blue')
            graph.DrawText(int(i/20+1), (i + 10 - 100,-100 ), color='blue')

    for i in range(0,len(uger)):
        graph.DrawCircle((i*5-100+20, fravær[i]-100), 2, line_color='red', fill_color='red')


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

        mistetløn=mistetLøn(a,200)
        gennemsnit=FraværGennemsnit(uge,fravær)


        window.Close()

        layout = [[sg.Text("Nedim er kommet forsent "+str(int(a))+" gange")],
                  [sg.Text("Samlet fravær: "+str(int(samletFravær))+" sekunder")],
                  [sg.Text("Mistet løn: "+str(int(mistetløn))+" kr")],
                  [sg.Text("Gennemsnitlig fravær per uge: "+str(int(gennemsnit))+" sekunder")]]
        grafLayout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(-105,-105), graph_top_right=(105,105), background_color='white', key='graph')]]
        backLayout= [[sg.Button("Back")]]
        layout = layout + grafLayout + backLayout
        window = sg.Window('Fravær', grab_anywhere=True).Layout(layout).Finalize()
        graph = window.FindElement('graph')
        graf(fravær,uge)


        event, values = window.Layout(layout).Read()

        if (event=="Back"):
            window.Close()

    if (event=="Exit"):
        exit()