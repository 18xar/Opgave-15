import math
<<<<<<< HEAD:OliverOskarOtto/pointsDistance.py
def PointsToDistance(Ax, Ay, Bx, By, Cx, Cy):

=======

def PointsDis(Ax, Ay, Bx, By, Cx, Cy):
>>>>>>> 9fb62b7992b30c4b2e87e1d4517144881214a650:OliverOskarOtto/pointsDis.py
    AB = math.sqrt((Ax-Bx)*(Ax-Bx)+(Ay-By)*(Ay-By))
    AC = math.sqrt((Ax-Cx)*(Ax-Cx)+(Ay-Cy)*(Ay-Cy))
    BC = math.sqrt((Bx-Cx)*(Bx-Cx)+(By-Cy)*(By-Cy))

    return(AB, AC, BC)