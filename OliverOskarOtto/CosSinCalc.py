import math

def CosSinCalc(AB, AC, BC):
    a = BC
    b = AC
    c = AB
    A = 0
    B = 01
    C = 0

    def SinVinkel(side1, side2, vinkel1):  # V2
        return math.degrees(math.asin(math.sin(math.radians(vinkel1)) / side1 * side2))

    def SinSide(side1, vinkel1, vinkel2):  # S2
        return side1 / math.sin(math.radians(vinkel1)) * math.sin(math.radians(vinkel2))

    def CosVinkel(side1, side2, side3):  # V1
        return math.degrees(math.acos((side2 * side2 + side3 * side3 - side1 * side1) / (2 * side2 * side3)))

    def CosSide(side1, side2, vinkel3):  # S3
        return math.sqrt(side1 * side1 + side2 * side2 - 2 * side1 * side2 * math.cos(math.radians(vinkel3)))

    def One80Vinkel(vinkel1, vinkel2):  # V3
        return 180 - vinkel1 - vinkel2

    if A == 0 and B == 0 and C == 0:  # 1 (Start 1. kolonne)
        A = CosVinkel(a, b, c)
        B = CosVinkel(b, c, a)
        C = CosVinkel(c, a, b)

    elif c == 0 and B == 0 and C == 0:  # 2
        B = SinVinkel(a, b, A)
        C = One80Vinkel(B, A)
        c = SinSide(a, A, C)

    elif c == 0 and A == 0 and C == 0:  # 3
        A = SinVinkel(b, a, B)
        C = One80Vinkel(A, B)
        c = SinSide(a, A, C)

    elif c == 0 and A == 0 and B == 0:  # 4
        c = CosSide(a, b, C)
        A = CosVinkel(a, b, c)
        B = One80Vinkel(A, C)

    elif a == 0 and B == 0 and C == 0:  # 5
        a = CosSide(b, c, A)
        B = CosVinkel(b, c, a)
        C = One80Vinkel(A, B)

    elif a == 0 and A == 0 and C == 0:  # 6
        C = SinVinkel(b, c, B)
        A = One80Vinkel(B, C)
        a = SinSide(b, B, A)

    elif a == 0 and A == 0 and C == 0:  # 7
        B = SinVinkel(c, b, C)
        A = One80Vinkel(B, C)
        a = SinSide(b, B, A)

    elif b == 0 and B == 0 and C == 0:  # 8
        C = SinVinkel(a, c, A)
        B = One80Vinkel(A, C)
        b = SinSide(a, A, B)

    elif b == 0 and A == 0 and C == 0:  # 9
        b = CosSide(a, c, B)
        A = CosVinkel(a, b, c)
        C = One80Vinkel(A, B)

    elif b == 0 and A == 0 and B == 0:  # 10
        A = SinVinkel(c, a, C)
        B = One80Vinkel(A, C)
        b = SinSide(a, A, B)

    elif b == 0 and c == 0 and C == 0:  # 11 (Start 2. kolonne)
        C = One80Vinkel(A, B)
        b = SinSide(a, A, B)
        c = SinSide(a, A, C)

    elif a == 0 and c == 0 and C == 0:  # 12
        a = SinSide(b, B, A)
        C = One80Vinkel(A, B)
        c = SinSide(a, A, C)

    elif a == 0 and b == 0 and C == 0:  # 13
        C = One80Vinkel(A, B)
        a = SinSide(c, C, A)
        b = SinSide(c, C, B)

    elif b == 0 and c == 0 and A == 0:  # 14
        A = One80Vinkel(B, C)
        b = SinSide(a, A, B)
        c = SinSide(a, A, C)

    elif a == 0 and c == 0 and A == 0:  # 15
        A = One80Vinkel(B, C)
        a = SinSide(b, B, A)
        c = SinSide(b, B, C)

    elif a == 0 and b == 0 and A == 0:  # 16
        A = One80Vinkel(B, C)
        a = SinSide(c, C, A)
        b = SinSide(c, C, B)

    elif b == 0 and c == 0 and B == 0:  # 17
        B = One80Vinkel(A, C)
        b = SinSide(a, A, B)
        c = SinSide(a, A, C)

    elif a == 0 and c == 0 and B == 0:  # 18
        B = One80Vinkel(A, C)
        a = SinSide(b, B, A)
        c = SinSide(a, A, C)

    elif a == 0 and b == 0 and B == 0:  # 19
        B = One80Vinkel(A, C)
        a = SinSide(c, C, A)
        b = SinSide(c, C, B)

    elif a == 0 and b == 0 and c == 0:  # 20
        print("Fuck af")

    return (A, B, C)

CosSinCalc(10, 10, 10)