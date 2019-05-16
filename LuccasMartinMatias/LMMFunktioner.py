import math

def FindMidtPunkt (x1,y1,x2,y2):

    x = (x1-x2)/2
    y = (y1-y2)/2

    return x,y

def findAfstand (x1, y1, x2, y2):
    afstand = math.sqrt((x1+x2)*(x1+x2)+(y1+y2)*(y1+y2))

    return afstand

def AreaOfTriangleHeron(side1,side2,side3):

    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

def CosRelvinkel(side1,side2,side3):
    vinkel1=math.degrees(math.acos((side2*side2+side3*side3-side1*side1)/(2*side2*side3)))
    return vinkel1

def FindTrekant(x1,y1,x2,y2,x3,y3):
    a = findAfstand(x2, y2, x3, y3)
    b = findAfstand(x1, y1, x3, y3)
    c = findAfstand(x1, y1, x2, y2)

    A = CosRelvinkel(a, b, c)
    B = CosRelvinkel(b, a, c)
    C = CosRelvinkel(c, b, a)

    areal = AreaOfTriangleHeron(a, b, c)

    result = [a, b, c, A, B, C, areal]

    return result
