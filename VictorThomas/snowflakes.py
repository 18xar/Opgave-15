import random, arcade

def snowflake (x, y):

    s = random.randint(5, 20)
    size = random.randint(2, 3)
    nLeaf = random.randint(1, 2)

    arcade.draw_line(30 + x, s + y, 30 + x, 60 - s + y, (255, 255, 255), size)
    arcade.draw_line(s + x, 30 + y, 60 - s + x, 30 + y, (255, 255, 255), size)

    if (nLeaf == 2):
        arcade.draw_line(s + 5 + x, 60 - s - 5 + y, 60 - s - 5 + x, s + 5 + y, (255, 255, 255), size)
        arcade.draw_line(60 - s - 5 + x, 60 - s - 5 + y, s + 5 + x, s + 5 + y, (255, 255, 255), size)




arcade.open_window(60,60, "Snowflake")
arcade.set_background_color((0, 0, 0))

snowflake(0, 0)

arcade.finish_render()
arcade.run()