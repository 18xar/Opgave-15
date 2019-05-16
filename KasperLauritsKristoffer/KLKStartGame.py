import PySimpleGUI as sg


def GameWindow():
    money = 50

    layout = [[sg.Text("Money: "), sg.Text(money, key="money")],
              [sg.Text("Roulette")],
              [sg.Text("Bet amount: "), sg.Input(key="rouletteBetAmount", size=(5, 1))],
              [sg.Text("Position: "), sg.Input(key="roulettePosition", size=(5, 1))],
              [sg.Button("Roulette")],
              [sg.Button("Exit")]
              ]

    window = sg.Window("Game Window").Layout(layout)

    while True:
        event, values = window.Read()
        print(event, values)
        window.Element("money").Update(money)

        if event is None or event == "Exit":
            break

        if event == "Roulette":
            try:
                money = money - int(values["rouletteBetAmount"])
            except ValueError:
                continue

            try:
                roulettePosition = int(values["roulettePosition"])
            except ValueError:
                roulettePosition = values["roulettePosition"]

    window.Close()


GameWindow()