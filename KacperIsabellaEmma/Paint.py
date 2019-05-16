import arcade
import random
import PySimpleGUI
import Funtioner

layout = [[PySimpleGUI.Text("Vælg hvilket figur du ville have"), PySimpleGUI.Text(":")], [PySimpleGUI.Button("Cirkel"), PySimpleGUI.Button ("Suprise")],
          [PySimpleGUI.Button("Prisme")]

]


window = PySimpleGUI.Window('Paint').Layout(layout)
button, values = window.Read()
print(button, values)

#print(values[0])

if button == "Cirkel":
    arcade.open_window(600, 600, "Paint")

    arcade.set_background_color((0, 0, 0))

    arcade.start_render()

    Funtioner.CirkelP()

    arcade.finish_render()

    arcade.run()

if button == "Prisme":

    arcade.open_window(600, 600, "Paint")

    arcade.set_background_color((0, 0, 0))

    arcade.start_render()

    Funtioner.PrismeP()

    arcade.finish_render()

    arcade.run()

