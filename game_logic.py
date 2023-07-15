# board should be first init as: board = [[0,0,0], [0,0,0], [0,0,0]]

def win_check(board):
    p1 = [1, 1, 1]
    p2 = [2, 2, 2]
    tl = board[0][0]
    tr = board[0][2]
    mid = board[1][1]
    bl = board[2][0]
    br = board[2][2]
# Vertical Check
    for x in board:
        if x == p1:
            return 1
        elif x == p2:
            return 2
# Horizontal check
    for x in range(3):
        first = board[0][x]
        second = board[1][x]
        third = board[2][x]

        if first == second == third == 1:
            return 1
        elif first == second == third == 2:
            return 2
# Diagonal check
    if tl == mid == br == 1 or tr == mid == bl == 1:
        return 1
    elif tl == mid == br == 2 or tr == mid == bl == 2:
        return 2

    return 0



