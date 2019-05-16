import arcade
import random
import arcade

def CirkelP():

    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    x = random.randint(0, 600)
    y = random.randint(0,600)
    radius = random.randint(19,200)

    arcade.draw_circle_filled(x,y,radius,(r,g,b))

def PrismeP():


    r = random.randint(14, 255)
    b = random.randint(14, 255)
    g = random.randint(14, 255)

    x = random.randint(19, 200)
    y = random.randint(19, 200)
    h = random.randint(19, 200)
    w = random.randint(19, 200)

    arcade.draw_rectangle_filled(x,y,h,w, (r,b,g))
