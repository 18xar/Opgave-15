import PySimpleGUI as sg
from roulette import rulette



def GameWindow():
    money = 200

    layout = [[sg.Text("Money: "), sg.Text(money, key="money")],
              [sg.Text("Roulette")],
              [sg.Text("Bet amount: "), sg.Input(key="rouletteBetAmount", size=(5, 1))],
              [sg.Text("Position: "), sg.Input(key="roulettePosition", size=(5, 1))],
              [sg.Button("Roulette")],
              [sg.Text("Blackjack")],
              [sg.Text("Bet amount: "), sg.Input(key="blackjackBetAmount", size(5,1))],
              [sg.Button("Blackjack")],
              [sg.Button("Exit")]
              ]

    window = sg.Window("Game Window").Layout(layout)

    while True:
        event, values = window.Read()
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
                print(roulettePosition)
            except ValueError:
                roulettePosition = values["roulettePosition"]
                print(roulettePosition)

            profit, roll = rulette(int(values["rouletteBetAmount"]), roulettePosition)
            window.Element("money").Update(money)
            sg.Popup("Roll: ", roll[0], roll[1], "Profit: ", profit )




    window.Close()


GameWindow()