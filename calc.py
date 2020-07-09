
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def run(board):
    while not game_over(board):


    print(f"{game_over(board)} wins!!!!!!!!!!!!!!!!!!!!!!!!!!")

def game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and (board[i][0] != " "):
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] and (board[0][i] != " "):
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and (board[0][0] != " "):
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and (board[0][2] != " "):
        return board[0][2]
    return ""

def print_board(board):
    line = "|"
    output = [str(3 - (i)) + line.join(board[i]) for i in range(3)]
    linebreak = "\n -----\n"
    print(linebreak.join(output))
    print(" 1 2 3")
print_board(board)