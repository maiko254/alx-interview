#!/usr/bin/python3
"""Rotating a 2D matrix in-place 90 degrees clock-wise."""
from typing import List, Tuple


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """Rotates a 2D matrix in-place."""
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
