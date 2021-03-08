import random
import time

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
    time.sleep(0.5)

def a():
    i = board.index(0)

    board[i] = board[i-1]
    board[i-1] = 0

    current()
    time.sleep(0.5)

def s():
    i = board.index(0)

    board[i] = board[i+4]
    board[i+4] = 0

    current()
    time.sleep(0.5)

def d():
    i = board.index(0)

    board[i] = board[i+1]
    board[i+1] = 0

    current()
    time.sleep(0.5)

def solve():
    x = board.index(0)
    row = x//4
    col = x - row*4
    
    for _ in range(row):
        w()

    for _ in range(col):
        a()
    
    x = board.index(1)
    row = x//4
    col = x - row*4

    #1
    if row == 3:
        for _ in range(col):
            d()
        
        for _ in range(3):
            s()

        if col == 0:
            for _ in range(2):
                d(); w(); w(); a(); s()
        
        else:
            a(); w(); d()

            for _ in range(col-1):
                s(); a(); a(); w(); d()

            w(); a(); s(); d(); w(); w(); a(); s()
    
    elif row == 0:
        for _ in range(col):
            d()

        for _ in range(col-1):
            s(); a(), a(), w(), d()
        
        s(); a()

    else:
        for _ in range(col):
            d()
        
        for _ in range(row):
            s()

        if col == 0:
            for _ in range(row-1):
                d(); w(); w(); a(); s()

        else:
            a(); w(); d()

            for _ in range(col-1):
                s(); a(); a(); w(); d()

            if board[0] == 1:
                s()
                a()
            
            else:
                w(); a(); s()

                for _ in range(row-2):
                    d(); w(); w(); a(); s()

    #2
    x = board.index(2)
    row = x//4
    col = x - row*4

    if board[1] == 2:
        d()
    
    elif row == 0:
        d(); w(); d()

        if col == 3:
            d(); s(); a(); a(); w(); d()

        s(); a()

    elif board[5] == 2:
        s(); d(); d(); w(); w(); a(); s()
    
    elif row == 1:
        for _ in range(col):
            d()
        
        for _ in range(col-2):
            s(); a(); a(); w(); d()

        w(); a(); s()
    
    elif col == 0:
        d()

        for _ in range(row-1):
            s()

        a(); w(); d(); s()

        for _ in range(row-1):
            d(); w(); w(); a(); s()

    else:
        d()

        if col != 1:
            for _ in range(col-2):
                d()
            
            for _ in range(row-1):
                s()

            d()

            for _ in range(col-2):
                w(); a(); a(); s(); d()
        
        else:
            d() 
            
            for _ in range(row-1):
                s()

        w(); a(); s()

        for _ in range(row-1):
            d(); w(); w(); a(); s()

    #4
    x = board.index(4)
    row = x//4
    col = x - row*4    
    
    if board[2] == 4:
        d()
    
    elif row == 0:
        d(); w(); d(); s(); a()
    
    elif col == 0:
        for _ in range(row-1):
            s()
        
        a()

        if row != 1:
            w(); d(); s(); a(); w()

            if row == 3:
                w(); d(); s(); a(); w()

        s(); d(); d(); w(); a(); s(); d(); d(); w(); w(); a(); s()

    elif board[6] == 4:
        s(); d(); d(); w(); w(); a(); s()
    
    elif board[7] == 4:
        d(); d(); w(); a(); s()
    
    elif col == 3:
        for _ in range(row-1):
            s()

        d(); d(); w(); a(); s()

        for _ in range(row-1):
            d(); w(); w(); a(); s()

    else:
        if col == 1:
            d()

            for _ in range(row-1):
                s()

            a()

            for _ in range(row-1):
                w()

        d()

        for _ in range(row-1):
            s()

        for _ in range(row-1):
            d(); w(); w(); a(); s()

    #3
    x = board.index(3)
    row = x//4
    col = x - row*4

    if board[3] == 3:
        d(); w(); a(); s(); s(); d(); w(); a(); w(); d(); s(); s(); a(); w(); d()

    elif col == 3:
        for _ in range(row-1):
            s()

        d()

        if row != 1:
            w(); a(); s()

            for _ in range(row-2):
                d(); w(); w(); a(); s()
            
            d(); w()

    elif col == 2:
        for _ in range(row-1):
            s()
        
        for _ in range(row-2):
            d(); w(); w(); a(); s()

        d(); w()

    elif row == 1:
        for _ in range(2-col):
            a ()

        if col == 0:
            s(); d(); d(); w(); a()
        
        s(); d(); d(); w()
    
    else:
        for _ in range(row-1):
            s()

        for _ in range(2-col):
            a()

        if col == 0:
            w(); d(); d(); s(); a()
        
        w(); d(); s()

        if row == 3:
            d(); w(); w(); a(); s()

        d(); w()

    #3 4
    w(); a(); s(); a(); a()

    #5
    x = board.index(5)
    row = x//4
    col = x - row*4

    if row == 1:
        for _ in range(col):
            d()

        for _ in range(col-1):
            s(); a(); a(); w(); d()
        
        s(); a()
    
    elif col == 0:
        if row == 3:
            s(); s(); d(); w(); w(); a()

        s()

    else:
        for _ in range(row-1):
            s()

        for _ in range(col):
            d()

        for _ in range(col-1):
            w(); a(); a(); s(); d()
        
        w(); a(); s()

        if row == 3:
            d(); w(); w(); a(); s()

    #6
    x = board.index(6)
    row = x//4
    col = x - row*4

    if board[5] == 6:
        d()

    elif row == 1:
        d(); w()

        for _ in range(col-1):
            d()

        for _ in range(col-2):
            s(); a(); a(); w(); d()
        
        s(); a()

    elif col == 0 or col == 1:
        if col == 0:
            s(); d(); w(); a()
        
        elif row == 3:
            d(); s(); a(); w()
        
        s(); d(); d(); w(); w(); a(); s()
    
    else:
        d()

        for _ in range(row-2):
            s()

        for _ in range(col-1):
            d()
        
        for _ in range(col-2):
            w(); a(); a(); s(); d()
        
        w(); a(); s()

        for _ in range(row-2):
            d(); w(); w(); a(); s()

    #8
    x = board.index(8)
    row = x//4
    col = x - row*4

    if board[6] == 8:
        d()

    elif board[7] == 8:
        d(); w(); d(); s(); a()
    
    elif board[13] == 8:
        d(); s(); a(); w(); d(); s(); d(); w(); w(); a(); s()

    elif col == 0:
        for _ in range(row-2):
            s()
        
        a()

        if row == 2:
            s(); d(); d(); w(); a(); s(); d(); d(); w(); w(); a(); s()
        
        else:
            w(); d(); d(); s(); a(); w(); d(); s(); d(); w(); w(); a(); s()
        
    else:
        if board[14] == 8:
            d(); s(); a(); w()
        
        elif board[11] == 8:
            d(); d(); s(); a(); a(); w()
        
        elif board[15] == 8:
            s(); d(); d(); w(); a(); s(); a(); w()

        s(); d(); d(); w(); w(); a(); s()

    #7
    x = board.index(7)
    row = x//4
    col = x - row*4

    if row == 1:
        d(); w(); a(); s(); s(); d(); w(); a(); w(); d(); s(); s(); a(); w(); d()
    
    elif board[11] == 7:
        d()
    
    elif board[15] == 7:
        d(); s(); a(); w(); d()
    
    elif col == 2:
        s(); d(); w()
    
    else:
        if board[13] == 7:
            a(); s(); d(); w()
        
        elif board[8] == 7:
            a(); a(); s(); d(); d(); w()
        
        elif board[12] == 7:
            s(); a(); a(); w(); d(); s(); d(); w()

        a(); s(); d(); d(); w()

    #7 8
    w(); a(); s()

    #13
    if board[8] == 13:
        a()

    elif board[9] == 13:
        s(); a(); a(); w(); d()

    elif board[12] == 13:
        a(); a(); s(); d(); w()
    
    elif board[13] == 13:
        a(); s(); a(); w(); d()

    else:
        if board[11] == 13:
            d(); s(); a(); w()

        elif board[15] == 13:
            s(); d(); w(); a()
        
        a(); s(); d(); w(); a(); a(); s(); d(); w(); a(); s(); d(); w()

    #9
    if board[11] == 9:
        d(); d(); s(); a(); a(); w(); d()

    elif board[13] == 9:
        s(); d(); w()

    elif board[12] == 9:
        s(); a(); w(); d(); d(); s(); a(); w(); a(); s(); d(); w(); d(); s(); a(); w(); d()
    
    elif board[14] == 9:
        d(); s(); a(); w(); d()
    
    elif board[15] == 9:
        s(); d(); d(); w(); a(); s(); a(); w(); d()
    
    else:
        d()

    #9 13
    s(); a(); a(); w(); d()

    #14
    if board[13] == 14:
        s(); d(); w()
    
    else:
        if board[11] == 14:
            d(); d(); s(); a(); a(); w()
        
        elif board[14] == 14:
            d(); s(); a(); w()
        
        elif board[15] == 14:
            s(); d(); d(); w(); a(); s(); a(); w()

        d()
    
    #10
    if board[11] == 10:
        d()

    elif board[13] == 10:
        s(); a(); w(); d(); d(); s(); a(); w(); a(); s(); d(); w(); d(); s(); a(); w(); d()
    
    elif board[14] == 10:
        s(); d(); w()

    elif board[15] == 10:
        d(); s(); a(); w(); d()

    #10 14
    s(); a(); a(); w(); d()

    #11 12 15
    while board != endboard:
        d()
        if board == endboard:
            break
        s()
        if board == endboard:
            break
        a()
        if board == endboard:
            break
        w()

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

ans = 0
while ans != "play" and ans != "solved":
    ans = input("Would you like to play or see it be solved? [Play/Solved] ").lower()

if ans == "play":
    print("To play, use WASD to swap with the square you would like!\n")

    current()

    while board != endboard:
        turn()

    print("YAY!!! You Won! :D")

else:
    current()

    time.sleep(1)

    solve()