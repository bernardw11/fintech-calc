
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def run(board):
    turn = "x"
    while not game_results(board):
        print_board(board)
        print(f"IT IS PLAYER {turn}'s TURN!!!!!!!!")
        
        i = int(input("Choose a row number: "))
        j = int(input("Choose a column number: "))
        while not is_legal(i, j, board):
            print("THAT IS NOT A LEGAL MOVE FOOL")
            i = int(input("Choose a row number: "))
            j = int(input("Choose a column number: "))
        board[i - 1][j - 1] = turn

        if turn == "x":
            turn = "o"
        else:
            turn = "x"
    if game_results(board) == "tie":
        print("TIE GAME")
    else:
        print(f"{game_results(board)} wins!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print_board(board)

def is_legal(i, j, board):
    return i in range(1, 4) and j in range(1, 4) and board[i - 1][j - 1] == " "

def game_results(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and (board[i][0] != " "):
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] and (board[0][i] != " "):
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and (board[0][0] != " "):
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and (board[0][2] != " "):
        return board[0][2]
    for row in board:
        for space in row:
            if space == " ":
                return ""
    return "tie"

def print_board(board):
    print(" 1 2 3")
    line = "|"
    output = [str(i + 1) + line.join(board[i]) for i in range(3)]
    linebreak = "\n -----\n"
    print(linebreak.join(output))


run(board)