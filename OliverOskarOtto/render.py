import arcade

def TriangeRender(Ax, Ay, Bx, By, Cx, Cy):
    width = 800
    height = 800
    lineWidth = 5

    Ax = Ax + 400 + Ax * 20
    Ay = Ay + 400 + Ay * 20
    Bx = Bx + 400 + Bx * 20
    By = By + 400 + By * 20
    Cx = Cx + 400 + Cx * 20
    Cy = Cy + 400 + Cy * 20


    arcade.open_window(width, height, "Triagle Cordinate Drawer")
    arcade.set_background_color((255, 255, 255))

    #Draw axes
    arcade.draw_line(width/2, 0, width/2, height, (255, 255, 255), lineWidth)
    arcade.draw_line(0, height/2, width, height/2, (255, 255, 255), lineWidth)
    #draw point
    arcade.draw_point(Ax,Ay,(255, 180, 180), 13)
    arcade.draw_point(Bx,By,(255, 180, 180), 13)
    arcade.draw_point(Cx,Cy,(255, 180, 180), 13)



    arcade.finish_render()
    arcade.run()

TriangeRender(3,3,4,4,3,6)