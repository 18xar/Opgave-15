
def paaBaren():
    svar1 = input("""Hvad gør du?

    1) Går hen og spørger om hendes nummer.
    2) Tager hende på røven.
    3) Køber hende en drink.

    Dit valg: """)

    if (svar1 == "1"):
        print("Hun ignorer dig...og går. (du kan ikke forsøge igen, hun har mistet interessen)")

        rape = input("Vil du rape hende? (ja eller nej): ")

        if (rape == "ja" or rape == "Ja"):
            print("Du finder hende, raper hende og ryger i fængsel kort efter")
        else:
            print("Du raper hende ikke (det var hun sikkert glad for), men da du vælger at nuppe en meget stærk drink efter nederlaget, ryger du direkte i gulvet og dør!")

