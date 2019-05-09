import arcade

def TriangeRender(Ax, Ay, Bx, By, Cx, Cy):
    width = 800
    height = 800
    lineWidth = 5

    arcade.open_window(width, height, "Triagle Cordinate Drawer")
    arcade.set_background_color((255, 255, 255))

    #Draw axes
    arcade.draw_line(width/2, 0, width/2, height, (255, 255, 255), lineWidth)
    arcade.draw_line(0, height/2, width, height/2, (255, 255, 255), lineWidth)
    #draw point
    arcade.draw_point(Ax,Ay,(255, 180, 180), 20)

    arcade.finish_render()
    arcade.run()

TriangeRender(300,300,400,400,300,600)