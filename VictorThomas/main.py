import arcade, math, random
arcade.open_window(1000, 800, "Enheds Cirkel")
arcade.set_background_color((0, 0, 0))

v = 1




while (True):
    for v in range(0, 360):
        arcade.start_render()
        # enhedsCirkel
        arcade.draw_line(300, 400, 700, 400, (0, 255, 50))
        arcade.draw_line(500, 200, 500, 600, (0, 255, 50))
        arcade.draw_line(700, 1000, 700, 0, (0, 255, 50))
        arcade.draw_text("1", 510, 585, (0, 255, 50))
        arcade.draw_text("1", 300, 410, (0, 255, 50))
        arcade.draw_text("-1", 510, 200, (0, 255, 50))
        arcade.draw_text("-1", 680, 410, (0, 255, 50))
        arcade.draw_circle_outline(500, 400, 200, (0, 255, 50))


        y = round(math.sin(math.radians(v)), 5)
        x = round(math.cos(math.radians(v)), 5)
        z = round(math.tan(math.radians(v)), 5)
        vx = x * 200
        vy = y * 200
        vz = z * 200
        vx = vx + 500
        vy = vy + 400
        vz = vz + 400

        arcade.draw_circle_filled(vx, vy, 3, (0, 255, 50))
        arcade.draw_line(500, 400, vx, vy, (255, 255, 255))
        arcade.draw_line(500, 400, vx, 400, (255, 0, 0))
        arcade.draw_line(500, 400, 500, vy, (0, 0, 255))
        arcade.draw_line(700, 400, 700, vz, (255, 255, 0))
        arcade.draw_line(500, 400, 700, vz, (100, 100, 100))

        x = str(x)
        y = str(y)
        z = str(z)

        arcade.draw_text("Sin = " + y, 200, 700, (0, 255, 50))
        arcade.draw_text("Cos = " + x, 200, 680, (0, 255, 50))
        arcade.draw_text("Tan = " + z, 200, 660, (0, 255, 50))



        arcade.finish_render()
arcade.run()