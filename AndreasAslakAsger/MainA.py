from AndreasAslakAsger import FuncMaximal
from AndreasAslakAsger import FuncNewton
from AndreasAslakAsger import FuncOhmsLov
from AndreasAslakAsger import FuncResistivitet

valg1 = int(input("1: Ohms lov   2: Resistivitet   3: Newtons love   4: Maximal-værdier"))

if valg1 == 1:
    valg2 = int(input("1: Spændingsforskel   2: Resistans   3: Strømstyrke"))

    if valg2 == 1:
        R = float(input("Indtast resistansen"))
        I = float(input("Indtast strømstyrken"))
        print(FuncOhmsLov.OhmSpaendingsforskel(R, I))
    if valg2 == 2:
        U = float(input("Indtast Spaendingsforskellen"))
        I = float(input("Indtast strømstyrken"))
        print(FuncOhmsLov.OhmResistans(U, I))
    if valg2 == 3:
        U = float(input("Indtast Spaendingsforskellen"))
        R = float(input("Indtast resistansen"))
        print(FuncOhmsLov.OhmSpaendingsforskel(U, R))
if valg1 == 2:
    R = float(input("Indtast resistansen"))
    L = float(input("Indtast længden"))
    A = float(input("Indtast tværsnitsarealet"))
    print(FuncResistivitet.Resistivitet(R, L, A))
if valg1 == 3:
    m = float(input("Indtast massen"))
    a = float(input("Indtast accelerationen"))
    print(FuncNewton.Newtons2Lov(m, a))
if valg1 == 4:
    valg2 = int(input("1: Strømstyrke    2: Spændingsforskel"))

    if valg2 == 1:
        Ieff = float(input("Indtast effektivstrømstyrken"))
        print(FuncMaximal.Strømstyrke(Ieff))
    if valg2 == 2:
        Ueff = float(input("Indtast effektivspændingen"))
        print(FuncMaximal.Spændingsforskel(Ueff))
