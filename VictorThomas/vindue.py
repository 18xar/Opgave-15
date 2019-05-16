import arcade, random, time
import SnowflakeV4
yPos = 600




arcade.open_window(1200,600,"vindue")#window
# arcade.set_background_color((255,255,255))#color

coordinates = []
snowSize = 10

while (True):
    #startSpeed = random.randint(1, 3)
    #acceleration = 1.01
    #speed = startSpeed * acceleration
    speed = random.randint(3, 7)
    arcade.start_render()
    xPos = random.randrange(0, 1200, 10)
    yPos = yPos

    coordinates.append([xPos, yPos, speed])

    arcade.draw_rectangle_filled(600, 0 + (snowSize/2), 1200, snowSize, (200, 200, 200))

    i = 0
    stopPoint = len(coordinates)
    while i < stopPoint:
        SnowflakeV4.snowflake(coordinates[i][0], coordinates[i][1])
        coordinates[i][1] -= coordinates[i][2]
        if coordinates[i][1] < -30 + snowSize:
            coordinates.remove(coordinates[i])
            snowSize += 2.5
            i = i - 1
            stopPoint = stopPoint - 1
        i += 1
        if snowSize >= 600:
            #snowSize = 10
            arcade.draw_text("Loading Complete", 400, 300, (0, 0, 0))
            arcade.draw_text
    time.sleep(0.03)
    #
    #
    # for n in range(len(coordinates)):
    #
    #     print(coordinates[n])
    #     SnowflakeV4.snowflake(coordinates[n][0], coordinates[n][1])
    #     coordinates[n][1] -= coordinates[n][2]



    arcade.finish_render()
arcade.run()
