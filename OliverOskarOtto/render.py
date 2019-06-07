import arcade

def TriangeRender(Ax, Ay, Bx, By, Cx, Cy):
    import pointsDis
    import cosSinCalc
    AB, AC, BC = (pointsDis.PointsDis(Ax, Ay, Bx, By, Cx, Cy))
    A, B, C = cosSinCalc.CosSinCalc(AB, AC, BC)

    width = 800
    height = 800
    lineWidth = 5

    AxT = int(Ax)
    AyT = int(Ay)
    BxT = int(Bx)
    ByT = int(By)
    CxT = int(Cx)
    CyT = int(Cy)

    Ax = Ax + 400 + Ax * 30
    Ay = Ay + 400 + Ay * 30
    Bx = Bx + 400 + Bx * 30
    By = By + 400 + By * 30
    Cx = Cx + 400 + Cx * 30
    Cy = Cy + 400 + Cy * 30


    arcade.open_window(width, height, "Triangle Coordinate Drawer")
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
    arcade.draw_text("Length of AB is " + str(AB), 25, 300, arcade.color.WHITE)
    arcade.draw_text("Length of AC is " + str(AC), 25, 280, arcade.color.WHITE)
    arcade.draw_text("Length of BC is " + str(BC), 25, 260, arcade.color.WHITE)

    #tekst med vinkler
    arcade.draw_text("Angle A is " + str(A) + "°", 25, 230, arcade.color.WHITE)
    arcade.draw_text("Angle B is " + str(B) + "°", 25, 210, arcade.color.WHITE)
    arcade.draw_text("Angle C is " + str(C) + "°", 25, 190, arcade.color.WHITE)

    #tekst ved punkterne
    arcade.draw_text("A(" + str(AxT) + "," + str(AyT) + ")", Ax - 10, Ay + 10, arcade.color.WHITE)
    arcade.draw_text("B(" + str(BxT) + "," + str(ByT) + ")", Bx - 10, By + 10, arcade.color.WHITE)
    arcade.draw_text("C(" + str(CxT) + "," + str(CyT) + ")", Cx - 10, Cy + 10, arcade.color.WHITE)

    arcade.finish_render()
    arcade.run()
