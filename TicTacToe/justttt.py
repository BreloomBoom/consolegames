board = [[" "," "," "],[" "," "," "],[" "," "," "]]
w = 0

def current():
    print(str(board[0]) + "\n" + str(board[1]) + "\n" + str(board[2]))

def turn(player):
    square = int(input("Which square would you like to place your piece into? " + player))

    a = (square-1)//3
    b = square-1-a*3

    while board[a][b] != " ":
        square = int(input("Which square would you like to place your piece into? " + player))

        a = (square-1)//3
        b = square-1-a*3

    board[a][b] = player
    current()

def win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            print(board[i][0]+" has won!")
            w+=1

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            print(board[0][i]+" has won!")
            w+=1

    if board[0][0] == board[1][1] == board[2][2] != " ":
        print(board[0][0]+" has won!")
        w+=1

    if board[0][2] == board[1][1] == board[2][0] != " ":
        print(board[0][2]+" has won!")
        w+=1

while w == 0:
    turn("X")
    win()
    if w != 0:
        break
    turn("O")
    win()