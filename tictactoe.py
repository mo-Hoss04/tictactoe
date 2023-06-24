board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player_1 = "X"
winner = None
gameR= True



def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8])
    

def playeInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1]= player_1
    else:
        print("Player is already in that spot!")

def check_horizantal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def check_row(board):
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
    
def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_tie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gameR = False

def chceck_win():
    if check_diagonal(board) or check_horizantal(board) or check_row(board):
        print(f"The winner is {winner}")

def switch_player():
    global player_1
    if player_1 == "X":
        player_1 = "O"
    else:
        player_1 = "X"

while gameR:
    printBoard(board)
    playeInput(board)
    chceck_win()
    check_tie(board)
    switch_player()