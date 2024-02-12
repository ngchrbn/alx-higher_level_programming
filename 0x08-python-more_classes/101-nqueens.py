#!/usr/bin/python3

import sys

def is_valid_position(queens, row, col):
    """Checks if placing a queen at (row, col) is valid."""
    for queen in queens:
        if queen[0] == row or queen[1] == col or abs(queen[0] - row) == abs(queen[1] - col):
            return False
    return True


def solve_n_queens(n, row=0, queens=[]):
    """Solves the N-Queens problem recursively."""
    if row == n:
        print([queen for queen in queens])
        return
    for col in range(n):
        if is_valid_position(queens, row, col):
            queens.append((row, col))
            solve_n_queens(n, row + 1, queens)
            queens.pop()  # Backtrack

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4\n")
            sys.exit(1)
    except ValueError:
        print("N must be a number\n")
        sys.exit(1)
    solve_n_queens(N)
