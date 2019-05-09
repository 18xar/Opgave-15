import PySimpleGUI as sg



money = 50

def GameWindow():

    layout = [  [sg.Text("Money: " + str(money))],
                [sg.Text("Choose Game:")],
                [sg.RButton("Roulette")],
                [sg.OK("Exit")]
              ]




    window = sg.Window("Game Window").Layout(layout)

    window.Read()

GameWindow()

