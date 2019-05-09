import PySimpleGUI as sg


def window1Setup():
    layout1 = [
        [sg.InputText("Skriv dit navn her.")],
        [sg.Text("Hvis du tilslutter en chat-gruppe skal du skrive IP'en.")],
        [sg.InputText("Skriv ip'en her! Lad være tom, hvis du tilslutter.")],
        [sg.Text("Vil du hoste eller tilslutte?")],
        [sg.RButton("Host"), sg.RButton("Tilslut")]        
    ]

    window1 = sg.Window("Chat-opsætning").Layout(layout1)

    button, values = window1.Read()
    name = str(values[0])
    print("Dit navn/id er: " + name)
    returnList = [name]
    if button == "Tilslut":
        ip = str(values[1])
        returnList.append(ip)
        print("Den målrettede ip er: " + ip)
    return returnList


print(window1Setup())
