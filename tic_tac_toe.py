import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# Print the game board;

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Take player input

def playerinput(board):
    inp = int(input("Enter a number 1-9, to insert: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("Oops, a player is already present!")

# Check for win or tie

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkIfWin(board):
    global gameRunning
    if checkHorizontal(board) or checkDiagonal(board) or checkRow(board):
        printboard(board)
        print(f"Winner is {winner}!")
        gameRunning = False

def checkTie(board):
    global gameRunning
    if "-" not in board:
        checkIfWin(board)
        printboard(board)
        print("It's a tie!")
        gameRunning = False

# Switch player

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# One play computer

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

# Check for win or tie again

while gameRunning:
    printboard(board)
    playerinput(board)
    checkIfWin(board)
    checkTie(board)
    switchPlayer()
    if currentPlayer == "O":
        computer(board)
        checkIfWin(board)
        checkTie(board)
