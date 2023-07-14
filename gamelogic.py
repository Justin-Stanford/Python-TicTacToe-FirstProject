def horizontalValidator(board):
    p1 = [1, 1, 1]
    p2 = [2, 2, 2]

    for x in board:
        if x == p1:
            return 1
        elif x == p2:
            return 2
    return 0

def verticalValidator(board):
    for x in range(3):
        first = board[0][x]
        second = board[1][x]
        third = board[2][x]

        if first == second == third == 1:
            return 1
        elif first == second == third == 2:
            return 2
    return 0

def diagonalValidator(board):
    tl = board[0][0]
    mid = board[1][1]
    br = board[2][2]
    tr = board[0][2]
    bl = board[2][0]

    if tl == mid == br == 1 or tr == mid == bl == 1:
        return 1
    elif tl == mid == br == 2 or tr == mid == bl == 2:
        return 2
    return 0


