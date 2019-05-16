import arcade, random, math, Snowflake

arcade.open_window(1200,600,"vindue")#window
arcade.set_background_color((255,255,255))#color






while (True):
    startSpeed = random.randint(1, 3)
    acceleration = 1.01
    speed = startSpeed * acceleration

    xPos = random.randint(0, 1200, 10)





    arcade.finish_render()
arcade.run()