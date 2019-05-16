def paaBaren():
    svar = input("""Hvad gør du?

    1) Går hen og spørger om hendes nummer.
    2) Tager hende på røven.
    3) Køber hende en drink.

    Dit valg: """)

    if (svar == "1"):
        print("Hun ignorer dig...og går. (du kan ikke forsøge igen, hun har mistet interessen)")

        rape = input("Vil du rape hende? (1: \"ja\" eller 2: \"nej\"): ")

        if (rape == "1"):
            print("Du finder hende, raper hende og ryger i fængsel kort efter")
        else:
            print("Du raper hende ikke (det var hun sikkert glad for), men da du vælger at nuppe en meget stærk drink efter nederlaget, ryger du direkte i gulvet og dør!")

    if (svar == "2"):
        print("Du tager hende på røven og får lov til, at nyde det i et helt sekundt, før du får en kæmpe knytnæve og går i jorden")

    if (svar == "3"):
        print("""
Hun smiler, tager imod drinken og i begynder at snakke meget godt.
Lidt tid går og hun kan rigtigt godt lide dig hun tager dig med hjem til hende.
""")
    return svar
