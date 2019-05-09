import PySimpleGUI as sg


def main():
    window1Setup()


def window1Setup():
    layout1 = [
        [sg.InputText("Skriv dit navn her.")],
        [sg.Text("Hvis du tilslutter en chat-gruppe skal du skrive IP'en.")],
        [sg.InputText("Skriv ip'en her! Lad være tom, hvis du tilslutter.")],
        [sg.Text("Vil du hoste eller tilslutte?")],
        [sg.RButton("Host"), sg.RButton("Tilslut")]        
    ]

    window1 = sg.Window("Chat-opsætning").Layout(layout1)

    while True:
        button, values = window1.Read()
        print("Dit navn/id er: " + str(values[0]))
        if button == "Tilslut":
            print("Den målrettede ip er: " + str(values[1]))


if __name__ == "__main__":
    main()
