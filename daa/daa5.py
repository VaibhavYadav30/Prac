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









"""
Theory & Code Overview:
This script solves the N-Queens problem using Backtracking, a depth-first search technique that
incrementally builds candidates and abandons ("backtracks" from) invalid paths as soon as constraints
are violated[cite: 5]. The goal is to place 'n' queens on an n x n chessboard so that no two queens
attack each other horizontally, vertically, or diagonally. The 'solve' function places queens column by
column from left to right; for each row in the current column, it checks the left side of the same row,
the upper-left diagonal, and the lower-left diagonal for previously placed queens[cite: 5]. If a square is safe,
it places a queen (1) and recursively attempts to solve the next column (col + 1)[cite: 5]. If placing the queen
leads to a dead end later, it resets the square back to 0 (backtracking) and tries the next row until
all 'n' columns are successfully filled (col == n)[cite: 5]. Due to exploring valid permutations across the
board, the algorithm runs in O(n!) worst-case time complexity and O(n^2) space complexity to store the
board[cite: 5].
"""