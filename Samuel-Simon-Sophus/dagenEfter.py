def dagenEfter():
    print("""Du vågner op i hendes seng hvad gør du?
    """)

    svar = input("""
    1) Du tager dit tøj og smutter inden hun vågner.
    2) Du står op og laver morgen mad.
        
    Dit valg: """)

    if (svar == "1"):
        print("""
        Du ser hende aldrig igen og slipper for at betale børnepenge.
        DU VANDT!!!
        """)

    if (svar == "2"):
        print("""
        Hun står op i spiser morgen mad. du finder ud af hun er pisse irriterende.
        """)

        svar2 = input("""
        Hvad gør du?
        1) Du finder en dårlig undskyldning for at tage hjem og så smutter du.
        2) Du siger du ikke gider at se hende mere.
        
        Dit valg: """)

        if (svar2 == "1"):
            print("""Hun kan desværre huske dit navn og skriver 9 måneder senere at du skal betale børnepenge.
            DU TABTE!!!
            """)

        if (svar2 == "2"):
            print("""Hun siger at hun ikke er på p-piller og hun er gravid nu og du skal betale børnepenge
            DU TABTE!!!
            """)
