import PySimpleGUI as sg
from roulette import rulette
from blackJack import Blackjack



def GameWindow():
    money = 200

    layout = [[sg.Text("Money: "), sg.Text(money, key="money")],
              [sg.Text("Roulette")],
              [sg.Text("Bet amount: "), sg.Input(key="rouletteBetAmount", size=(5, 1))],
              [sg.Text("Position: "), sg.Input(key="roulettePosition", size=(5, 1))],
              [sg.Button("Roulette")],
              [sg.Text("Blackjack")],
              [sg.Text("Bet amount: "), sg.Input(key="blackjackBetAmount", size=(5,1))],
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
                rBet = int(values["rouletteBetAmount"])
            except ValueError:
                sg.Popup("Error: Not a number!")
                continue
            money -= rBet
            window.Element("money").Update(money)

            try:
                roulettePosition = int(values["roulettePosition"])
                print(roulettePosition)
            except ValueError:
                roulettePosition = str(values["roulettePosition"])
                print(roulettePosition)

            profit, roll = rulette(int(values["rouletteBetAmount"]), roulettePosition)
            window.Element("money").Update(money)
            sg.Popup("Roll: ", roll[0], roll[1], "Profit: ", profit )


        if event == "Blackjack" :
            try:
                bjBet = int(values["blackjackBetAmount"])
            except ValueError :
                sg.Popup("Error: Not a number!")
                continue
            money -= bjBet
            window.Element("money").Update(money)

            bjRet = Blackjack()

            if bjRet == 0 :
                sg.Popup("It's a draw!")
                money += bjBet
            if bjRet == 1 :
                sg.Popup("You lost", bjBet)
            if bjRet == 2 :
                money = money + (2 * bjBet)
                sg.Popup("You won", 2*bjBet)
            if bjRet == 3 :
                money = money + (2.5 * bjBet)
                sg.Popup("Blackjack! You won" , 2.5*bjBet)

            window.Element("money").Update(money)







    window.Close()


GameWindow()