import random

board1 = [[" "," "," "],[" "," "," "],[" "," "," "]]
w = 0
empty = [i for i in range(9)]

#board state
def current(board):
    print(str(board[0]) + "\n" + str(board[1]) + "\n" + str(board[2]))

#human turn
def turn(board):
    square = int(input("Which square would you like to place your piece into? "))
    a = (square-1)//3
    b = square-1-a*3

    while board[a][b] != " ":
        square = int(input("Which square would you like to place your piece into? "))

        a = (square-1)//3
        b = square-1-a*3

    board[a][b] = "X"
    empty.remove(square-1)
    current(board1)    

#bot turn
def bot():
    global w
    board2 = board1
    for i in range(len(empty)):
        a = (empty[i])//3
        b = empty[i]-a*3

        board2[a][b] = "O"
        win(board2)

        if w == 1:
            board1[a][b] = "O"
            empty.remove(empty[i])
            break

        board2[a][b] = " "

    for i in range(len(empty)):
        if w != 1:
            a = (empty[i])//3
            b = empty[i]-a*3

            board2[a][b] = "X"
            win(board2)
            
            if w == 1:
                board1[a][b] = "O"
                empty.remove(empty[i])
                break

            board2[a][b] = " "

    if w == 0:
        square = empty[random.randint(0,len(empty)-1)]
        a = (square)//3
        b = square-a*3
        board1[a][b] = "O"

        empty.remove(square)
    
    w=0
    current(board1)

#win condition
def win(board):
    global w
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            w+=1

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            w+=1

    if board[0][0] == board[1][1] == board[2][2] != " ":
        w+=1

    if board[0][2] == board[1][1] == board[2][0] != " ":
        w+=1
    
    if empty == [] and w != 1:
        w+=1

#game loops
place = int(input("Would you like to go first or second? [1/2] "))

if place == 1:
    while w == 0:
        turn(board1)
        win(board1)
        if w != 0:
            break
        bot()
        win(board1)

else:
    while w == 0:
        bot()
        win(board1)
        if w != 0:
            break
        turn(board1)
        win(board1)