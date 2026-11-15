# N-Queens using Backtracking
def solve(board, col, n):

    if col == n:
        return True

    for row in range(n):

        safe = True

        # Check same row
        for i in range(col):
            if board[row][i] == 1:
                safe = False

        # Check upper diagonal
        for i in range(1, col + 1):
            if row-i >= 0 and board[row-i][col-i] == 1:
                safe = False

        # Check lower diagonal
        for i in range(1, col + 1):
            if row+i < n and board[row+i][col-i] == 1:
                safe = False

        if safe:
            board[row][col] = 1

            if solve(board, col+1, n):
                return True

            board[row][col] = 0

    return False


n = 4
board = [[0]*n for i in range(n)]

if solve(board, 0, n):
    for row in board:
        print(row)
else:
    print("No solution")
