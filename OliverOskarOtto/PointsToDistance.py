import math
def PointsToDistance(Ax, Ay, Bx, By, Cx, Cy):

    AB=math.sqrt((Ax-Bx)*(Ax-Bx)+(Ay-By)*(Ay-By))
    AC=math.sqrt((Ax-Cx)*(Ax-Cx)+(Ay-Cy)*(Ay-Cy))
    BC=math.sqrt((Bx-Cx)*(Bx-Cx)+(By-Cy)*(By-Cy))

    return(AB, AC, BC)