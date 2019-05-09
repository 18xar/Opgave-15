import PySimpleGUI as sg
from LuccasMartinMatias import LMMFunktioner

Afstand = [
    [sg.Text("Udregn afstand mellem to punkter")],
    [sg.Text("Punkt A"), sg.Text("Punkt B")],
    [sg.InputText("0,0"), sg.InputText("0,0")],
    [sg.RButton("Udregn")],
    [sg.Text("resultat:", key="resultat")]
]

MidtPunkt = [
    [sg.Text("Udregn punktet mellem to punkter")],
    [sg.Text("Punkt A"), sg.Text("Punkt B")],
    [sg.InputText("0,0"), sg.InputText("0,0")],
    [sg.RButton("Udregn")],
    [sg.Text("resultat:", key="resultat")]
]

TrekantBeregner = [
    [sg.Text("Udregn afstand mellem to punkter")],
    [sg.Text("Punkt A"), sg.Text("Punkt B")],
    [sg.InputText("0,0"), sg.InputText("0,0")],
    [sg.RButton("Udregn")],
    [sg.Text("resultat:", key="resultat")]
]

layout = [
    [sg.RButton("Afstand"), sg.RButton("MidtPunkt")],
    [sg.RButton("Trekant")]
]

window = sg.Window('Main').Layout(layout)


def popup(button):
    print("kaldt popup function")

    if button == "Afstand":
        window2 = sg.Window("Afstand").Layout(Afstand)
        while True:
            event, values = window2.Read()
            secondValues = []
            if event is None or event == "Exit":
                break
            # Read input
            for i in range(0, len(values)):
                values[i].replace(",", " ")
                tempList = i.split()
                count = 0
                for y in tempList:
                    if count == 0:
                        values[i] = y
                    elif count == 1:
                        secondValues[i] = y
                    count = 1

            # lav input om fra string til float
            x1 = float(values[0])
            x2 = float(secondValues[0])
            y1 = float(values[1])
            y2 = float(secondValues[1])

            # udregn og vis resultat
            resultat = LMMFunktioner.findAfstand(x1, x2, y1, y2)
            print(resultat)
            window2.FindElement("resultat").Update(str(resultat))

    if button == "MidtPunkt":
        window2 = sg.Window("MidtPunkt").Layout(MidtPunkt)
        while True:
            event, values = window2.Read()
            secondValues = []
            if event is None or event == "Exit":
                break
            # Read input
            for i in range(0, len(values)):
                values[i].replace(",", " ")
                tempList = i.split()
                count = 0
                for y in tempList:
                    if count == 0:
                        values[i] = y
                    elif count == 1:
                        secondValues[i] = y
                    count = 1

            # lav input om fra string til float
            x1 = float(values[0])
            x2 = float(secondValues[0])
            y1 = float(values[1])
            y2 = float(secondValues[1])

            # udregn og vis resultat
            resultat = LMMFunktioner.MidPunktV(x1, x2, y1, y2)
            print(resultat)
            window2.FindElement("resultat-kegle-stub").Update(str(resultat))
    if button == "Trekant":
        window2 = sg.Window("TrekantBeregner").Layout(TrekantBeregner)
        while True:
            event, values = window2.Read()
            secondValues = []
            if event is None or event == "Exit":
                break
            # Read input
            for i in range(0, len(values)):
                values[i].replace(",", " ")
                tempList = i.split()
                count = 0
                for y in tempList:
                    if count == 0:
                        values[i] = y
                    elif count == 1:
                        secondValues[i] = y
                    count = 1

            # lav input om fra string til float
            x1 = float(values[0])
            x2 = float(secondValues[0])
            y1 = float(values[1])
            y2 = float(secondValues[1])

            # udregn og vis resultat
            resultat = LMMFunktioenr.Trekanter(x1, x2, y1, y2)
            print(resultat)
            window2.FindElement("resultat-kugle").Update(str(resultat))


while True:
    button, values = window.Read()

    if button is None or button == "Exit":
        break

    popup(button)
