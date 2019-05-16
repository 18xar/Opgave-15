import arcade
import random
import PySimpleGUI


arcade.open_window(600, 600, "Paint")



arcade.set_background_color((0, 0, 0))

arcade.start_render()

CirkelP()

arcade.finish_render()

arcade.run()