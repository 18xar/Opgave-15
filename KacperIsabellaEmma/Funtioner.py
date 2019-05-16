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





