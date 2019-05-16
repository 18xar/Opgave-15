import random, arcade

def snowflakev2 (x, y):

    a = True
    s = random.randint(5, 20)
    size = random.randint(2, 3)
    nLeaf = random.randint(1, 2)

    arcade.draw_line(30 + x, s + y, 30 + x, 60 - s + y, (255, 255, 255), size)
    arcade.draw_line(s + x, 30 + y, 60 - s + x, 30 + y, (255, 255, 255), size)

    if (nLeaf == 2):
        arcade.draw_line(s + 5 + x, 60 - s - 5 + y, 60 - s - 5 + x, s + 5 + y, (255, 255, 255), size)
        arcade.draw_line(60 - s - 5 + x, 60 - s - 5 + y, s + 5 + x, s + 5 + y, (255, 255, 255), size)
    while (a):
        nLeaf = random.randint(1, 2)
        rotation = random.randint(1, 2)

        if (rotation == 2):
            arcade.draw_line(30 + x, s + y, 30 + x, 60 - s + y, (255, 255, 255), size)
            arcade.draw_line(s + x, 30 + y, 60 - s + x, 30 + y, (255, 255, 255), size)
            a = False
        if (nLeaf == 2):
            arcade.draw_line(s + 5 + x, 60 - s - 5 + y, 60 - s - 5 + x, s + 5 + y, (255, 255, 255), size)
            arcade.draw_line(60 - s - 5 + x, 60 - s - 5 + y, s + 5 + x, s + 5 + y, (255, 255, 255), size)
            a = False


