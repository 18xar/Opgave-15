import random

antalDeck = 1
deck = []

dealer = []
player = []

playerEs = 0
dealerEs = 0

es = 11

loose = "i do not know... yet"
for ANTAL in range(antalDeck):
    for KULØR in range(4):
        for TYPE in range(13):
            if TYPE >= 10:
                VÆRDI = 10
                deck.append([KULØR, TYPE + 1, VÆRDI])
            elif TYPE == 0:
                VÆRDI = es
                deck.append([KULØR, TYPE + 1, VÆRDI])
            else:
                VÆRDI = TYPE
                deck.append([KULØR, TYPE + 1, VÆRDI + 1])


def Draw():
    træk = random.randint(0, len(deck) - 1)
    kort = deck[træk]
    deck.pop(træk)
    return kort



def PlaceCard(card):

    color = (250, 0, 0)
    if card[0] > 1:
        color = (0, 0, 0)

    numberText = str(card[1])
    if card[1] == 1:
        numberText = "A"
    if card[1] == 11:
        numberText = "J"
    if card[1] == 12:
        numberText = "Q"
    if card[1] == 13:
        numberText = "K"

    typeText = ""
    if card[0] == 0:
        typeText = "Hjerter"
    if card[0] == 1:
        typeText = "Ruder"
    if card[0] == 2:
        typeText = "Spar"
    if card[0] == 3:
        typeText = "klør"

    print(typeText + " " + numberText)


def PlaceAll(person):
    for X in range(len(person)):
        PlaceCard(person[X])

def PlaceInformation():
    print("Dealer:")
    PlaceCard(dealer[0])

    print()
    print("spiller:")
    PlaceAll(player)
    #print("sum: " + str(playerSum))
    print()

def PlaceInformation2():
    print("Dealer:")
    PlaceAll(dealer)
    print("sum: " + str(dealerSum))

    print()
    print("spiller:")
    PlaceAll(player)
    print("sum: " + str(playerSum))
    print()




for x in range(2):
    dealer.append(Draw())

for x in range(2):
    player.append(Draw())

playerSum = player[0][2] + player[1][2]
if player[0][1] == 1:
    playerEs += 1
if player[1][1] == 1:
    playerEs += 1


dealerSum = dealer[0][2] + dealer[1][2]
if dealer[0][1] == 1:
    dealerEs += 1
if dealer[1][1] == 1:
    dealerEs += 1

PlaceInformation()

if player[0][1] > 10 and player[1][1] == 1 or player[1][1] > 10 and player[0][1] == 1:
    loose = "Blackjack"

playerHold = False

HitHold = 0

if loose == "i do not know... yet":
    while playerHold == False:
        HitHold = input("1 Hit, 2 Hold:")

        if HitHold == "1":
            player.append(Draw())
            playerSum += player[len(player) - 1][2]
            if player[len(player) - 1][1] == 1:
                playerEs += 1
            PlaceInformation()

        if HitHold == "2":
            playerHold = True

        if playerSum > 21:
            if playerEs > 0:
                playerSum -= 10
                playerEs -= 1

            else:
                loose = True
                playerHold = True

dealerHold = False

if loose == "i do not know... yet":
    while dealerHold == False:
        if dealerSum > 21:
            if dealerEs > 0:
                dealerSum -= 10
                dealerEs -= 1
            else:
                dealerHold = True

        if dealerSum < 17:
            dealer.append(Draw())
            dealerSum += dealer[len(dealer) - 1][2]
            PlaceInformation2()

        else:
            if playerSum > dealerSum:
                loose = False
            if playerSum < dealerSum:
                loose = True
            if playerSum == dealerSum:
                loose = "draw"
            if dealerSum > 21:
                loose = False
            dealerHold = True

##########################

if loose == True:
    print("DU TABTE :(")
    PlaceInformation2()

if loose == False:
    print("DU VANDT :)")
    PlaceInformation2()

if loose == "draw":
    print("well....")
    PlaceInformation2()

if loose == "Blackjack":
    print("BLACKJACK!! :O")
    PlaceInformation2()