import math

#alle funktioner
def SinRelVinkel(side1, side2, vinkel1):
    return math.degrees(math.asin(math.sin((math.radians(vinkel1))/ side1 * side2)))

def SinRelSide(vinkel1, vinkel2, side1):
    return (side1 / math.sin(math.radians(vinkel1))) * (math.sin(math.radians(vinkel2)))

def CosRelSide(side1, side2, vinkel3):
    return math.sqrt(side1 * side1 + side2 * side2 - 2 * side1 * side2 * math.cos(math.radians(vinkel3)))

def CosRelVinkel(side1, side2, side3):
    return math.degrees(math.acos((side2 * side2 + side3 * side3 - side1 * side1) / (2 * side2 * side3)))

def Sum180(vinkel1, vinkel2):
    return 180 - vinkel1 - vinkel2

def main():
    global havea, haveb, havec, haveA, haveB, haveC, a, b, c, A, B, C

#all if statements
    try:
        a, b, c, A, B, C = input("skriv a b c A B C hvis du ikke har verdien skriv 0 \n her >").split()
        a = float(a)
        b = float(b)
        c = float(c)
        A = float(A)
        B = float(B)
        C = float(C)
        havea = False
        haveb = False
        havec = False
        haveA = False
        haveB = False
        haveC = False

        if a > 0:
            havea = True
        if b > 0:
            haveb = True
        if c > 0:
            havec = True
        if A > 0:
            haveA = True
        if B > 0:
            haveB = True
        if C > 0:
            haveC = True

        if havea and haveb and havec:
            A = CosRelVinkel(a, b, c)
            B = CosRelVinkel(b, a, c)
            C = CosRelVinkel(c, b, a)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havea and haveb and haveA:
            B = SinRelVinkel(a, b, A)
            C = Sum180(A,B)
            c = SinRelSide(A, C, a)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havea and haveb and haveB:
            A = SinRelVinkel(b, a, B)
            C = Sum180(A, B)
            c = SinRelSide(A, C, a)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havea and haveb and haveC:
            c = CosRelSide(C, a, b)
            B = SinRelVinkel(c, b, C)
            A = Sum180(B, C)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havec and haveb and haveA:
            a = CosRelSide(A, b, c)
            B = SinRelVinkel(a, b, A)
            C = Sum180(A, B)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havec and haveb and haveB:
            C = SinRelVinkel(b, c, B)
            A = Sum180(B, C)
            a = SinRelSide(B, A, b)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havec and haveb and haveC:
            B = SinRelVinkel(c, b, C)
            A = Sum180(B, C)
            a = SinRelSide(B, A, b)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havec and havea and haveA:
            C = SinRelVinkel(a, c, A)
            B = Sum180(A, C)
            b = SinRelSide(A, B, a)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havec and havea and haveB:
            b = CosRelSide(B, a, c)
            A = SinRelVinkel(b, a, B)
            C = Sum180(A, B)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havec and havea and haveC:
            A = SinRelVinkel(c, a, C)
            B = Sum180(A, C)
            b = SinRelSide(A, B, a)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havea and haveA and haveB:
            b = SinRelSide(A, B, a)
            C = Sum180(A, B)
            c = SinRelSide(B, C, b)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havea and haveA and haveC:
            c = SinRelSide(A, C, a)
            B = Sum180()
            b = SinRelSide(C, B, c)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havea and haveC and haveB:
            A = Sum180(B, C)
            c = SinRelSide(A, C, a)
            b = SinRelSide(A, B, a)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif haveb and haveA and haveB:
            a = SinRelSide(B, A, b)
            C = Sum180(A, B)
            c = SinRelSide(A, C, a)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif haveb and haveA and haveC:
            B = Sum180(A, C)
            a = SinRelSide(B, A, b)
            c = SinRelSide(A, C, a )
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif haveb and haveC and haveB:
            c = SinRelSide(B, C, b)
            A = Sum180(B, C)
            a = SinRelSide(B, A, b)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havec and haveA and haveB:
            C = Sum180(A, B)
            a = SinRelSide(C, A, c)
            b = SinRelSide(C, B, c)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havec and haveA and haveC:
            a = SinRelSide(C, A, c)
            B = Sum180(A, C)
            b = SinRelSide(A, B, a)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        elif havec and haveC and haveB:
            b = SinRelSide(C, B, c)
            A = Sum180(B, C)
            a = SinRelSide(B, A, b)
            print('A: ' + str(A) + '\n' + 'B: ' + str(B) + '\n' + 'C: ' + str(C) + '\n' + 'a: ' + str(a) + '\n' + 'b: ' +
                  str(b) + '\n' + 'c: ' + str(c))

        else:
            print('Det er ikke en trekant')
    except:
        print('Fuck dig!')

main()