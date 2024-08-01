#!/usr/bin/python3
import sys

if len(sys.argv) > 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col):
    """utility function to check if a queen can be placed on board[row][col].
    """
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N):
    """ """
    def backtrack(board, row):
        """ """
        if row == N:
            solution = []
            for r in range(N):
                solution.append([r, board[r]])
            print(solution)
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1

    board = [-1] * N

    backtrack(board, 0)


solve_nqueens(N)
