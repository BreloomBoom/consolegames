board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
w = 0

def current():
    print(str(board[0]) + "\n" + str(board[1]) + "\n" + str(board[2]) + "\n" + str(board[3]) + "\n" + str(board[4]) + "\n" + str(board[5]))

def turn(user):
    col = int(input("What column would you like to place your piece in? (1-7) "))-1

    while col > 6 or col < 0 or board[0][col] != 0:
        col = int(input("Please choose an available slot (1-7) "))-1

    for i in range(6):
        if board[5-i][col] == 0:
            board[5-i][col] = user
            break
    
    current()

def win():
    for i in range(7):
        x = i
        for i in range(3):
            if board[5-i][x] == board[4-i][x] == board[3-i][x] == board[2-i][x] != 0:
                print("Player " + str(board[5-i][x]) + " has won!")
                w += 1
        
    for i in range(6):
        x = i
        for i in range(4):
            if board[x][6-i] == board[x][5-i] == board[x][4-i] == board[x][3-i] != 0:
                print("Player " + str(board[x][6-i]) + " has won!")
                w += 1

    for i in range(3):
        x = i
        for i in range(4):
            if board[2-x][i] == board[3-x][i+1] == board[4-x][i+2] == board[5-x][i+3] != 0:
                print("Player " + str(board[2-x][i]) + " has won!")
                w += 1

        for i in range(4):
            if board[2-x][6-i] == board[3-x][5-i] == board[4-x][4-i] == board[5-x][3-i] != 0:
                print("Player " + str(board[2-x][6-i]) + " has won!")
                w += 1

while w == 0:
    turn(1)
    win()
    if w != 0:
        break
    turn(2)
    win()