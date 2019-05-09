import random, arcade

def snowflake (x, y):
    size1 = 30
    size2 = 30


    arcade.draw_line(30 + x, 10 + y, 30 + x, 50 + y, (255, 255, 255), 2)





arcade.open_window(160,160, "Snowflake")
arcade.set_background_color((0, 0, 0))

snowflake()

arcade.finish_render()
arcade.run()