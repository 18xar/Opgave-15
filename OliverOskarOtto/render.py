import arcade

width = 800
height = 800
lineWidth = 5

arcade.open_window(width, height, "Triagle Cordinate Drawer")
arcade.set_background_color((255, 255, 255))

Ax = 1
Ay = 2
Bx = 6
By = 3
Cx = 3
Cy = 10

#Draw axes
arcade.draw_line(width/2, 0, width/2, height, (0, 0, 0), lineWidth)

arcade.finish_render()
arcade.run()