# SCOR EN DAME SPIL
import random
from paaBaren import *
from hjemmeHosHende import *
from dagenEfter import *


def spil():
    print("""
    Du åbner døren ind til den lokale bar og kigger rundt. Du ser den mest sexede kvinde sidde ovre i kanten af baren. Det tager dig lidt tid men du samler modet og går hen til hende.""")
    svar = paaBaren()

    if (svar == "3"):
        sex = hjemmeHosHende()
    else:
        print("Tak fordi du spillede.")

        if (sex == 1):
            dagenEfter()
        else:
            print("Tak fordi du spillede.")


spil()
