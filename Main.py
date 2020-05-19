#Name: Fahad Ansar
#St#: 6203384

import os
from copy import deepcopy
from random import randrange

#intializing primitives--------------------------------------------------
turn = 'O'
value = 4
vl=-500


# Rack
rack = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']]


#flag variable
tbt = 0

#-------------------------------------------------------------------------

# for printing the board that has been passed as a parameter
def printbrd(rackt):
    print(" 0 1 2 3 4 5 6")
    print("|" + str(rackt[0][0]) + "|" + str(rackt[0][1]) + "|" + str(rackt[0][2]) + "|" + str(rackt[0][3]) + "|" + str(
        rackt[0][4]) + "|" + str(rackt[0][5]) + "|" + str(rackt[0][6]) + "|")
    print("|" + str(rackt[1][0]) + "|" + str(rackt[1][1]) + "|" + str(rackt[1][2]) + "|" + str(rackt[1][3]) + "|" + str(
        rackt[1][4]) + "|" + str(rackt[1][5]) + "|" + str(rackt[1][6]) + "|")
    print("|" + str(rackt[2][0]) + "|" + str(rackt[2][1]) + "|" + str(rackt[2][2]) + "|" + str(rackt[2][3]) + "|" + str(
        rackt[2][4]) + "|" + str(rackt[2][5]) + "|" + str(rackt[2][6]) + "|")
    print("|" + str(rackt[3][0]) + "|" + str(rackt[3][1]) + "|" + str(rackt[3][2]) + "|" + str(rackt[3][3]) + "|" + str(
        rackt[3][4]) + "|" + str(rackt[3][5]) + "|" + str(rackt[3][6]) + "|")
    print("|" + str(rackt[4][0]) + "|" + str(rackt[4][1]) + "|" + str(rackt[4][2]) + "|" + str(rackt[4][3]) + "|" + str(
        rackt[4][4]) + "|" + str(rackt[4][5]) + "|" + str(rackt[4][6]) + "|")
    print("|" + str(rackt[5][0]) + "|" + str(rackt[5][1]) + "|" + str(rackt[5][2]) + "|" + str(rackt[5][3]) + "|" + str(
        rackt[5][4]) + "|" + str(rackt[5][5]) + "|" + str(rackt[5][6]) + "|")


# for checking whether the board is full
def ifFull(board):
    g = True
    for i in range(6):
        for j in range(7):
            if board[i][j] == ' ':
                g = False
                break
        if g == False:
            break
    return g


# for flipping the turn
def flipper(turn):
    temp = ''
    if turn == 'O':
        temp = 'X'
    else:
        temp = 'O'
    return temp


# Checking if the entered column is full
def isColNtFull(rackt, cl):
    full = False
    for i in range(6):
        if rackt[i][cl] == ' ':
            full = True
    return full


# Taking input from user with appropriate constraints (Human to Human)
def takeInput():
    os.system("clear")
    print("Turn :", str(turn))
    printbrd(rack)
    try:
        jk = int(input("Enter a Column [0-6]: \n"))
    except ValueError:
        print("Value Error: You didnt Entered a number :/")

    while jk > 7 or jk < 0 or not isColNtFull(rack, jk):
        print("Not a valid column, Please try again\n")
        jk = int(input("Enter a Column [0-6]: \n"))

    return jk


# inserting the disc/chip/piece in the board (Human to Human)
def insertChip():
    ip = takeInput()
    global turn
    if rack[5][int(ip)] == ' ':
        rack[5][int(ip)] = turn

    elif rack[4][int(ip)] == ' ':
        rack[4][int(ip)] = turn

    elif rack[3][int(ip)] == ' ':
        rack[3][int(ip)] = turn

    elif rack[2][int(ip)] == ' ':
        rack[2][int(ip)] = turn

    elif rack[1][int(ip)] == ' ':
        rack[1][int(ip)] = turn

    elif rack[0][int(ip)] == ' ':
        rack[0][int(ip)] = turn

    turn = flipper(turn)


# checking if someone has won (For All)
def winCheck(board, ex):
    g = False
    for i in range(0, 6):
        if g: break
        for j in range(0, 7):
            if board[i][j] != ' ' and board[i][j] == ex:
                g = False
                right = 0
                down = 0
                dRight = 0
                dLeft = 0

                for m in range(0, 4):
                    # right
                    if j + m < 7 and board[i][j + m] == ex:
                        right = right + 1

                    # down
                    if i + m < 6 and board[i + m][j] == ex:
                        down = down + 1

                    # diganomalRight
                    if i + m < 6 and j + m < 7 and board[i + m][j + m] == ex:
                        dRight = dRight + 1

                    # diagonal Left
                    if i + m < 6 and j - m >= 0 and board[i + m][j - m] == ex:
                        dLeft = dLeft + 1

                # check the the variables
                if right == 4 or down == 4 or dRight == 4 or dLeft == 4:
                    # print("----------", str(i), str(j))
                    g = True
                    break
    return g


# AI-Stuff---------------------AI-Stuff---------------AI-Stuff-----------------


# heuristic method that test heuristics on the board and returns the total score

def heuristic(rack):
    value = 0
    noC = 0
    yesC = 0
    for i in range(6):
        for j in range(7):
            if rack[i][j] == 'O':
                right = 0
                down = 0
                dRight = 0
                dLeft = 0

                for m in range(0, 4):
                    # right
                    if j + m < 7:
                        if rack[i][j + m] == 'O':
                            right = right + 1
                        elif rack[i][j + m] == 'X' and right>=3:
                            value = value + 4


                    # down
                    if i + m < 6 :
                        if rack[i + m][j] == 'O':
                            down = down + 1
                        elif rack[i + m][j] == 'X' and down>=3:
                            value=value+3

                    # diganomalRight
                    if i + m < 6 and j + m < 7 :
                        if rack[i + m][j + m] == 'O':
                            dRight = dRight + 1
                        elif rack[i + m][j + m] == 'X' and dRight>=3:
                            value=value+2

                    # diagonal Left
                    if i + m < 6 and j - m >= 0 :
                        if rack[i + m][j - m] == 'O':
                            dLeft = dLeft + 1
                        elif rack[i + m][j - m] == 'O'and dLeft>=3:
                            value=value+2

                if right == 2 or down == 2 or dLeft == 2 or dRight == 2:
                    value = value - 6
                if right == 3 or down == 3 or dLeft == 3 or dRight == 3:
                    value = value - 20
                if right == 4 or down == 4 or dLeft == 4 or dRight == 4:
                    value = value - 100



            elif rack[i][j] == 'X':
                right = 0
                down = 0
                dRight = 0
                dLeft = 0

                for m in range(0, 4):
                    # right
                    if j + m < 7 and rack[i][j + m] == 'X':
                            right = right + 1

                    # down
                    if i + m < 6 and rack[i + m][j] == 'X':
                            down = down + 1

                    # diganomalRight
                    if i + m < 6 and j + m < 7 and rack[i + m][j + m] == 'X':
                            dRight = dRight + 1

                    # diagonal Left
                    if i + m < 6 and j - m >= 0 and rack[i + m][j - m] == 'X':
                            dLeft = dLeft + 1

                if right == 2 or down == 2 or dLeft == 2 or dRight == 2:
                    value = value + 1
                if right == 3 or down == 3 or dLeft == 3 or dRight == 3:
                    value = value + 15
                if right == 4 or down == 4 or dLeft == 4 or dRight == 4:
                    value = value + 30



    return value


# Minimax Method

def recurseNF(rackj, tempt, valueX):

    #Base case (If full or at bottom most depth level)
    if valueX == 0:
        return heuristic(rackj)

    elif ifFull(rackj):
        return 0


    #Minimax keeper
    wrth = 0


    # Flip
    if tempt == 'O':
        tempt = 'X'
        wrth = -99999999999999
    else:
        tempt = 'O'
        wrth = 9999999999999


    # For loop for making all 7 possible combinations at a state
    for i in range(7):

        tempb = deepcopy(rackj)         #Making new board

        rand = i                        #Updating the board

        # Dropping Piece
        tt = 0
        if tempb[5][int(rand)] == ' ':
            tempb[5][int(rand)] = tempt
            tt = 5
        elif tempb[4][int(rand)] == ' ':
            tempb[4][int(rand)] = tempt
            tt = 4
        elif tempb[3][int(rand)] == ' ':
            tempb[3][int(rand)] = tempt
            tt = 3
        elif tempb[2][int(rand)] == ' ':
            tempb[2][int(rand)] = tempt
            tt = 2
        elif tempb[1][int(rand)] == ' ':
            tempb[1][int(rand)] = tempt
            tt = 1
        elif tempb[0][int(rand)] == ' ':
            tempb[0][int(rand)] = tempt
            tt = 0
        if tt==0: continue


        #Min Recursive calls (getting min out of all)
        if tempt == 'O':
            score = recurseNF(tempb, tempt, valueX - 1)
            wrth=min(wrth,score)            #-9999999999

        #Max Recursice calls (getting max out of all)
        elif tempt == 'X':
            score = recurseNF(tempb, tempt, valueX - 1)
            wrth = max(score,wrth)         #9999999999

        tempb[tt][int(rand)] = ' '

    #Updating the board with the move
    if valueX == (value-1):
        global vl
        global rack
        if  wrth > vl:
            vl=wrth

            rack=deepcopy(rackj)
            # print(wrth)
            # printbrd(rack)

    return wrth





# Main Controller-------------------Main Controller------------------------


#Human vs AI Game
def aiGame():
    global rack

    printbrd(rack)
    while(True):
        # os.system("clear")
        print("Turn :", str(turn))


        #input handling
        try:
            ip = int(input("Enter a Column [0-6]: \n"))
        except ValueError:
            print("Value Error : You didnt Entered a number :/")

        while ip > 7 or ip < 0 or not isColNtFull(rack, ip):
            print("Not a valid column, Please try again\n")
            ip = int(input("Enter a Column [0-6]: \n"))

        #dropping piece for human
        if rack[5][int(ip)] == ' ':
            rack[5][int(ip)] = turn

        elif rack[4][int(ip)] == ' ':
            rack[4][int(ip)] = turn

        elif rack[3][int(ip)] == ' ':
            rack[3][int(ip)] = turn

        elif rack[2][int(ip)] == ' ':
            rack[2][int(ip)] = turn

        elif rack[1][int(ip)] == ' ':
            rack[1][int(ip)] = turn

        elif rack[0][int(ip)] == ' ':
            rack[0][int(ip)] = turn

        #checking if human has won
        if winCheck(rack, 'O'):
            print("----------Somebody just won!!--------")
            printbrd(rack)
            print("GAME ENDS \n -----> O wins")
            break

        #UI
        print("Your Move-----------------------")
        printbrd(rack)
        print("--------------------------------")


        #AI move calculation and performing move
        global vl
        vl = -500
        recurseNF(rack, tempt=turn, valueX=4)

        print("AI Move------------------------")

        printbrd(rack)

        #checking if AI has won
        if winCheck(rack, 'X'):
            print("----------Somebody just won!!--------")
            printbrd(rack)
            print("GAME ENDS \n -----> X wins")
            break

        # ending game if baord is full
        if ifFull(rack): break











#Main control method that controls the interaction between user and program
def flow(turnIn):
    print("-----------Connect4 with AI---------------")
    print(" ")

    global rack

    #input handling
    try:
        opt = int(
            input(
                "with whom you want to play[0/1]: \n 0- You v/s Human (human-human) \n 1- You v/s AI (human-AI)\n"))
    except ValueError:
        print("Please Enter value")

    #human vs human
    if opt == 0:

        while (True):
            insertChip()

            if winCheck(rack, 'X'):
                printbrd(rack)
                print("GAME ENDS \n -----> X wins")
                break
            elif winCheck(rack, 'O'):
                printbrd(rack)
                print("GAME ENDS \n -----> O wins")
                break

    #human vs AI
    elif opt == 1:

        aiGame()

    else:
        pass

flow(turnIn="O")

