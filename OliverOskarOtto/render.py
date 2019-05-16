import arcade

def TriangeRender(Ax, Ay, Bx, By, Cx, Cy):
    width = 800
    height = 800
    lineWidth = 5

    Ax = Ax + 400 + Ax * 30
    Ay = Ay + 400 + Ay * 30
    Bx = Bx + 400 + Bx * 30
    By = By + 400 + By * 30
    Cx = Cx + 400 + Cx * 30
    Cy = Cy + 400 + Cy * 30


    arcade.open_window(width, height, "Triagle Cordinate Drawer")
    arcade.set_background_color((255, 255, 255))

    #Draw axes
    arcade.draw_line(width/2, 0, width/2, height, (255, 255, 255), lineWidth)
    arcade.draw_line(0, height/2, width, height/2, (255, 255, 255), lineWidth)
    #draw point
    arcade.draw_point(Ax,Ay,(255, 180, 180), 13)
    arcade.draw_point(Bx,By,(255, 180, 180), 13)
    arcade.draw_point(Cx,Cy,(255, 180, 180), 13)

    #Draw line
    arcade.draw_line(Ax,Ay,Bx,By,(60, 180, 180), 4)
    arcade.draw_line(Ax,Ay,Cx,Cy,(60, 180, 180), 4)
    arcade.draw_line(Bx,By,Cx,Cy,(60, 180, 180), 4)

    #tekst med længde





    arcade.finish_render()
    arcade.run()

TriangeRender(3,3,4,4,3,6)