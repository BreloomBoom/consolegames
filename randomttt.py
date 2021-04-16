import random

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
w = 0
empty = [i for i in range(9)]

#board state
def current():
    print(str(board[0]) + "\n" + str(board[1]) + "\n" + str(board[2]))

#human turn
def turn():
    square = int(input("Which square would you like to place your piece into? "))
    a = (square-1)//3
    b = square-1-a*3

    while board[a][b] != " ":
        square = int(input("Which square would you like to place your piece into? "))

        a = (square-1)//3
        b = square-1-a*3

    board[a][b] = "X"
    empty.remove(square-1)
    current()    

#bot turn
def bot():
    square = empty[random.randint(0,len(empty)-1)]
    a = (square)//3
    b = square-a*3
    board[a][b] = "O"
    empty.remove(square)
    current()

#win condition
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

#game loops
place = int(input("Would you like to go first or second? [1/2] "))

if place == 1:
    while w == 0:
        turn()
        win()
        if w != 0:
            break
        bot()
        win()

else:
    while w == 0:
        bot()
        win()
        if w != 0:
            break
        turn()
        win()