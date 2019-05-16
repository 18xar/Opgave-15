import arcade
import math
screenW = 800
screenH = 600
def drawBox (h, l, b):
    normX = screenW/2
    normY = screenH / 8

    widthAddX = math.cos(math.radians(30)) * b
    widthAddY = math.sin(math.radians(30)) * b

    lenghtAddX = math.cos(math.radians(150)) * l
    lenghtAddY = math.sin(math.radians(150)) * l

#W1
    widthEndOneX = normX + widthAddX
    widthEndOneY = normY + widthAddY
# L1
    lenghtEndOneX = normX + lenghtAddX
    lenghtEndOneY = normY + lenghtAddY
# H1
    heightOneEndY = normY + h
# W2
    widthEndTwoX = widthEndOneX
    widthEndTwoY = heightOneEndY + widthAddY
# L2
    lenghtEndTwoX = widthEndOneX + lenghtAddX
    lenghtEndTwoY = widthEndOneY + lenghtAddY
# H3
    heightThreeEndY = lenghtEndTwoY + h
# H4
    heightFourEndY = lenghtEndOneY + h


# H3
    arcade.draw_line(lenghtEndTwoX, lenghtEndTwoY, lenghtEndTwoX, heightThreeEndY, (100, 100, 100), 2)
# L2
    arcade.draw_line(widthEndOneX, widthEndOneY, lenghtEndTwoX, lenghtEndTwoY, (100, 100, 100), 2)
# W1
    arcade.draw_line(normX, normY, widthEndOneX, widthEndOneY, (0, 0, 0), 2)
# L1
    arcade.draw_line(normX, normY, lenghtEndOneX, lenghtEndOneY, (0, 0, 0), 2)
# H1
    arcade.draw_line(normX, normY, normX, heightOneEndY, (0, 0, 0), 2)
# W2
    arcade.draw_line(normX, heightOneEndY, widthEndTwoX, widthEndTwoY, (0, 0, 0), 2)
# H2
    arcade.draw_line(widthEndOneX, widthEndOneY, widthEndTwoX, widthEndTwoY, (0, 0, 0), 2)
# W3
    arcade.draw_line(lenghtEndOneX, lenghtEndOneY, lenghtEndTwoX, lenghtEndTwoY, (100, 100, 100), 2)
# H4
    arcade.draw_line(lenghtEndOneX, lenghtEndOneY, lenghtEndOneX, heightFourEndY, (0, 0, 0), 2)
# W4
    arcade.draw_line(lenghtEndOneX, heightFourEndY, lenghtEndTwoX, heightThreeEndY, (0, 0, 0), 2)
# L3
    arcade.draw_line(normX, heightOneEndY, lenghtEndOneX, heightFourEndY, (0, 0, 0), 2)
# L4
    arcade.draw_line(widthEndOneX, widthEndTwoY, lenghtEndTwoX, heightThreeEndY, (0, 0, 0), 2)

arcade.open_window(800, 600, "no")
arcade.set_background_color((255, 255, 255))
arcade.start_render()
drawBox(40, 100, 100)
arcade.finish_render()
arcade.run()