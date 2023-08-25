board={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

def printBoard():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def insertLetter(letter, position):
    if board[position] == ' ':
        board[position] = letter
        printBoard()
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkWinfor('X'):
            print("Bot wins!")
            exit()
        if checkWinfor('O'):
            print("Player wins!")
            exit()
        return
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position: "))
        insertLetter(letter, position)
        return

def checkWinfor(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark or 
        board[4] == board[5] and board[4] == board[6] and board[4] == mark or
        board[7] == board[8] and board[7] == board[9] and board[7] == mark or
        board[1] == board[4] and board[1] == board[7] and board[1] == mark or
        board[2] == board[5] and board[2] == board[8] and board[2] == mark or
        board[3] == board[6] and board[3] == board[9] and board[3] == mark or
        board[1] == board[5] and board[1] == board[9] and board[1] == mark or
        board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def playMove():
    position = int(input("Enter a position for 'O': "))
    insertLetter('O',position)

def botMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = 'X'
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter('X', bestMove)
    return


def minimax(board, depth, isMaximizing):
    if (checkWinfor('X')):
        return 1
    elif (checkWinfor('O')):
        return -1
    elif (checkDraw()):
        return 0
    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = 'X'
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore
    else: 
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = 'O'
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

print("Board postions:\n1 2 3\n4 5 6\n7 8 9\n")
while True:
    botMove()
    playMove()