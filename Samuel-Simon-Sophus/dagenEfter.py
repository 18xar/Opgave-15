def dagenEfter():
    print("""du vågner op i hendes seng 
    hvad gør du?""")

    svar = input("""1)du tager dei tøj og smutter inden hun vågner
    2)du står op og laver morgen mad""")

    if (svar == "1"):
        print("du ser hende aldrig igen og slipper for at betale børne penge "
              "DU VANDT!!!")

    if (svar == "2"):
        print("hun står op i spiser morgen mad. du finder ud af hun er pisse irreterene")

        svar2 = input("""hvad gør du?
        1) du finder en dårlig undskyldning for at tage hjem og så smutter du
        2) du siger du ikke gider at se hende mere""")

        if (svar2 == "1"):
            print("""hun kan detsværre huske dit navn og skriver 9 måneder senere at du skal betale børne penge 
            DU TABTE!!!""")

        if (svar2 == "2"):
            print("""hun siger at hun ikke er på p-piller og hun er gravid nu og du skal betale børne penge
            DU TABTE!!!""")
