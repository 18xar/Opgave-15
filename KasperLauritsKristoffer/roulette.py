import random

def rulette(bet, position):
    board = []
    profit = 0

    #laver numrene:

    for x in range(38):
        board.append([])
        board[x].append(x-1)

    #laver farverne:

    for green in range(2):
        board[green].append(0)

    for red in range(2,12,2):
        board[red].append(1)

    for black in range(3,13,2):
        board[black].append(2)


    for black in range(12,20,2):
        board[black].append(2)

    for red in range(13,20,2):
        board[red].append(1)


    for black in range(21,31,2):
        board[black].append(2)

    for red in range(20,30,2):
        board[red].append(1)


    for black in range(30,38,2):
        board[black].append(2)

    for red in range(31,38,2):
        board[red].append(1)

    #laver et roll:

    roll = board[random.randint(0, len(board))-1]

    #Hvad man kan bette på:

    if position == "Red":
        if 1 == roll[1]:
            profit = bet * 2

    elif position == "Black":
        if 2 == roll[1]:
            profit = bet * 2

    elif position == "1-19":
        if roll[0] > 0 and roll[0] < 20:
            profit = bet * 2

    elif position == "20-36":
        if roll[0] > 20 and roll[0] < 37:
            profit = bet * 2

    elif int(position) >= -1 and int(position) <= 36:
        if int(position) == roll[0]:
            profit = bet * 36

    return profit, roll

