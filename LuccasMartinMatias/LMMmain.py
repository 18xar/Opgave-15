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
    [sg.Text("Punkt A"), sg.Text("Punkt B"), sg.Text("Punkt C")],
    [sg.InputText("0,0"), sg.InputText("0,0"), sg.InputText("0,0")],
    [sg.RButton("Udregn")],
    [sg.Text("Areal:"), sg.Text("0", key="areal")],
    [sg.Text("a:"), sg.Text("0", key="a")],
    [sg.Text("b:"), sg.Text("0", key="b")],
    [sg.Text("c:"), sg.Text("0", key="c")],
    [sg.Text("A:"), sg.Text("0", key="A")],
    [sg.Text("B:"), sg.Text("0", key="B")],
    [sg.Text("C:"), sg.Text("0", key="C")],
    [sg.RButton("Tegn trekant")]
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
                tempList = values[i].replace(",", " ")
                tempList = tempList.split()
                count = 0
                for y in tempList:
                    if count == 0:
                        values[i] = y
                    elif count == 1:
                        secondValues.append(y)
                    count = 1

            # lav input om fra string til float
            x1 = float(values[0])
            x2 = float(values[1])
            y1 = float(secondValues[0])
            y2 = float(secondValues[1])

            # udregn og vis resultat
            resultat = LMMFunktioner.findAfstand(x1, y1, x2, y2)
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
                tempList = values[i].replace(",", " ")
                tempList = tempList.split()
                count = 0
                for y in tempList:
                    if count == 0:
                        values[i] = y
                    elif count == 1:
                        secondValues.append(y)
                    count = 1

            # lav input om fra string til float
            x1 = float(values[0])
            x2 = float(values[1])
            y1 = float(secondValues[0])
            y2 = float(secondValues[1])

            # udregn og vis resultat
            resultat = LMMFunktioner.FindMidtPunkt(x1, y1, x2, y2)
            print(resultat)
            window2.FindElement("resultat").Update(str(resultat))
    if button == "Trekant":
        window2 = sg.Window("TrekantBeregner").Layout(TrekantBeregner)
        while True:
            event, values = window2.Read()
            secondValues = []
            if event is None or event == "Exit":
                break
            # Read input
            elif event == "Udregn":
                for i in range(0, len(values)):
                    tempList = values[i].replace(",", " ")
                    tempList = tempList.split()
                    count = 0
                    for y in tempList:
                        if count == 0:
                            values[i] = y
                        elif count == 1:
                            secondValues.append(y)
                        count = 1

                # lav input om fra string til float
                x1 = float(values[0])
                x2 = float(values[1])
                x3 = float(values[2])
                y1 = float(secondValues[0])
                y2 = float(secondValues[1])
                y3 = float(secondValues[2])


                # udregn og vis resultat
                resultat = LMMFunktioner.FindTrekant(x1, y1, x2, y2, x3, y3)
                print(resultat)
                window2.FindElement("a").Update(str(resultat[0]))
                window2.FindElement("b").Update(str(resultat[1]))
                window2.FindElement("c").Update(str(resultat[2]))
                window2.FindElement("A").Update(str(resultat[3]))
                window2.FindElement("B").Update(str(resultat[4]))
                window2.FindElement("C").Update(str(resultat[5]))
                window2.FindElement("areal").Update(str(resultat[6]))
                button, values = window.Read()
                if button == "Tegn trekant":
                    LMMFunktioner.TegnTrekant(x1, y1, x2, y2, x3, y3)




while True:
    button, values = window.Read()

    if button is None or button == "Exit":
        break

    popup(button)
