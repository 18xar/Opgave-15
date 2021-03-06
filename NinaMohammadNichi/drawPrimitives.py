import arcade
import math
def drawBox (h, l, b):
    screenW = 800
    screenH = 600
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

    arcade.open_window(800, 600, "Visuel primitive")
    arcade.set_background_color((255, 255, 255))
    arcade.start_render()

# Højde tekst
    if b >= 60:
        arcade.draw_text("h =" + str(h), normX + 10, normY + h/2, (0, 0, 0))
    else:
        arcade.draw_text("h =" + str(h), normX + 10 + b, normY + h / 2, (0, 0, 0))
# Længde tekst
    arcade.draw_text("l =" + str(l), (normX + lenghtEndOneX) / 2 - l/10, (normY + lenghtEndOneY) / 2 - 23, (0, 0, 0), 12, 0, "left",
                     ("calibri", "arial"), False, False, "left", "baseline", -30)
# Bredde teskst
    arcade.draw_text("b =" + str(b), (normX + widthEndOneX) / 2, (normY + widthEndOneY) / 2 - 10, (0, 0, 0), 12, 0, "left",
                     ("calibri", "arial"), False, False, "left", "baseline", 30)

# H3
    arcade.draw_line(lenghtEndTwoX, lenghtEndTwoY, lenghtEndTwoX, heightThreeEndY, (150, 150, 150), 2)
# L2
    arcade.draw_line(widthEndOneX, widthEndOneY, lenghtEndTwoX, lenghtEndTwoY, (150, 150, 150), 2)
# W3
    arcade.draw_line(lenghtEndOneX, lenghtEndOneY, lenghtEndTwoX, lenghtEndTwoY, (150, 150, 150), 2)
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
# H4
    arcade.draw_line(lenghtEndOneX, lenghtEndOneY, lenghtEndOneX, heightFourEndY, (0, 0, 0), 2)
# W4
    arcade.draw_line(lenghtEndOneX, heightFourEndY, lenghtEndTwoX, heightThreeEndY, (0, 0, 0), 2)
# L3
    arcade.draw_line(normX, heightOneEndY, lenghtEndOneX, heightFourEndY, (0, 0, 0), 2)
# L4
    arcade.draw_line(widthEndOneX, widthEndTwoY, lenghtEndTwoX, heightThreeEndY, (0, 0, 0), 2)
    arcade.finish_render()
    arcade.run()

#drawBox(110, 210, 100)

'''
arcade.open_window(800, 600, "Visuel primitive")
arcade.set_background_color((255, 255, 255))
arcade.start_render()
#drawBox(110, 210, 150)
arcade.finish_render()
arcade.run()'''