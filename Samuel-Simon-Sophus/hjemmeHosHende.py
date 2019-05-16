def hjemmeHosHende():
    sex = 0
    hvadnu = input(
        """Du klarede det, du charmerede dig ind på damen og har fået lov til at komme hjem til hende. Men du er ikke færdig endnu, du vil helst godt i seng med hende og måske få en date mere.
        
        Hvad vil du nu?
        1) for at gå ud i køkkenet
        2) for at gå direkte til soveværelset
        3) for at gå på toilettet

          Dit valg: """)
    if (hvadnu == "1"):
        print("Du valgte at gå ud i køkkenet, hvor du æder alt hendes mad og bliver smidt ud. Dårlig stil...")

    if (hvadnu == "2"):
        print("""Du går ud til pigen på hendes soveværelse, det er relativt lille men der er plads til to i sengen. 
Det er ikke specielt romantisk men i hygger jer og du overnatter.
""")
        sex = 1

    if (hvadnu == "3"):
        lorteloesning = input(
            """du går ud på toilettet fordi du skal skide, du sætter dig på kummen og laver en stor lort. Men du kan ikke skylle. Hvad gør du?
        1) for at smide lorten ud af vinduet
        2) for at lade lorten ligge og tørre dig og gå ind på soveværelset
        3) for at prøve at fixe toilettet""")

        if (lorteloesning == "1"):
            print("""Du smed lorten ud af vinduet. Den perfekte løsning. 
                  Du vasker dine hænder og går ind og får dit retmæssige fisse""")
            sex = 1

        if (lorteloesning == "2"):
            print("""Du valgte at lade lorten ligge. Et valg som kune en kryster ville tage. 
Det viser sig at hun også skal på toilettet bagefter, og du bliver smidt hjem af en fuld pige der synes dit lort er klamt.""")

        if (lorteloesning == "3"):
            print("""Du prøver at fikse toilettet, du har jo fikset ting før.
Desværre er det her et ret kompliceret problem og du ender dækket i lortevand 
Du siger hvad der er sket og du bliver smidt ud og får sendt en regning på 2000kr. dagen efter.""")

    return sex
