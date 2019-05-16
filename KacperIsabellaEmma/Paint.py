import arcade
import random

def CirkelP():

    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    x = random.randint(0, 600)
    y= random.randint(0,600)
    radius= random.randint(19,200)

    arcade.draw_circle_filled(x,y,radius,(r,g,b))





arcade.open_window(600, 600, "Paint")



arcade.set_background_color((0, 0, 0))

arcade.start_render()

CirkelP()

arcade.finish_render()

arcade.run()