import random

board = [
    0,0,0,0,
    0,0,0,0,
    0,0,0,0,
    0,0,0,0
]

endboard = [
    1,2,3,4,
    5,6,7,8,
    9,10,11,12,
    13,14,15,0
]

k = 1
n = 0

while (n + k) % 2 != 0:
    n = 0
    ranlist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    board = [
    0,0,0,0,
    0,0,0,0,
    0,0,0,0,
    0,0,0,0
    ]

    for i in range(15):
        x = random.randint(0,len(ranlist)-1)
        board[ranlist[x]] = i+1
        ranlist.remove(ranlist[x])

    k = ranlist[0]//4 + 1

    for i in range(15):
        for j in range(i + 1, 16):
            if board[i] != 0 and board[j] != 0 and board[i] > board[j]:
                n += 1

def current():
    print(
        str(board[0])+" "+str(board[1])+" "+str(board[2])+" "+str(board[3])+"\n"+
        str(board[4])+" "+str(board[5])+" "+str(board[6])+" "+str(board[7])+"\n"+
        str(board[8])+" "+str(board[9])+" "+str(board[10])+" "+str(board[11])+"\n"+
        str(board[12])+" "+str(board[13])+" "+str(board[14])+" "+str(board[15])+"\n"
    )    

def w():
    i = board.index(0)

    board[i] = board[i-4]
    board[i-4] = 0

    current()

def a():
    i = board.index(0)

    board[i] = board[i-1]
    board[i-1] = 0

    current()
def s():
    i = board.index(0)

    board[i] = board[i+4]
    board[i+4] = 0

    current()

def d():
    i = board.index(0)

    board[i] = board[i+1]
    board[i+1] = 0

    current()

def turn():
    #corners
    if board[0] == 0:
        print("The available moves are S and D")

        move = input().lower()
        while move != "s" and move != "d":
            move = input("That isn't an available move please try again\n").lower()

        if move == "s":
            s()

        else:
            d()
    
    elif board[3] == 0:
        print("The available moves are A and S")

        move = input().lower()
        while move != "s" and move != "a":
            move = input("That isn't an available move please try again\n").lower()

        if move == "s":
            s()

        else:
            a()

    elif board[12] == 0:
        print("The available moves are W and D")

        move = input().lower()
        while move != "w" and move != "d":
            move = input("That isn't an available move please try again\n").lower()

        if move == "w":
            w()

        else:
            d()

    elif board[15] == 0:
        print("The available moves are W and A")

        move = input().lower()
        while move != "w" and move != "a":
            move = input("That isn't an available move please try again\n").lower()

        if move == "w":
            w()

        else:
            a()

    #top side
    elif board[1] == 0 or board[2] == 0:
        print("The available moves are A, S and D")

        move = input().lower()
        while move != "s" and move != "a" and move != "d":
            move = input("That isn't an available move please try again\n").lower()

        if move == "a":
            a()

        elif move == "d":
            d()

        else:
            s()

    #left side
    elif board[4] == 0 or board[8] == 0:
        print("The available moves are W, S and D")

        move = input().lower()
        while move != "s" and move != "w" and move != "d":
            move = input("That isn't an available move please try again\n").lower()

        if move == "w":
            w()

        elif move == "d":
            d()

        else:
            s()

    #bottom side
    elif board[13] == 0 or board[14] == 0:
        print("The available moves are W, A and D")

        move = input().lower()
        while move != "w" and move != "a" and move != "d":
            move = input("That isn't an available move please try again\n").lower()

        if move == "a":
            a()

        elif move == "d":
            d()

        else:
            w()

    #right side
    elif board[7] == 0 or board[11] == 0:
        print("The available moves are W, A and S")

        move = input().lower()
        while move != "s" and move != "a" and move != "w":
            move = input("That isn't an available move please try again\n").lower()

        if move == "a":
            a()

        elif move == "w":
            w()

        else:
            s()

    #else
    else:
        print("The available moves are W, A, S and D")

        move = input().lower()
        while move != "s" and move != "a" and move != "w" and move != "d":
            move = input("That isn't an available move please try again\n").lower()

        if move == "a":
            a()

        elif move == "w":
            w()
        
        elif move == "d":
            d()

        else:
            s()

print("To play, use WASD to swap with the square you would like!\n")

current()

while board != endboard:
    turn()

print("YAY!!! You Won! :D")