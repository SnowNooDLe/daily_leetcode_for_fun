"""
867. Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
image can be found from: https://leetcode.com/problems/transpose-matrix/

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
"""
from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    """Runtime 104ms, Memory 14.7MB"""
    return [list(row) for row in list(zip(*matrix))]


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    """Runtime 95ms, Memory 14.9MB"""
    transposed_matrix = []
    for row_idx in range(len(matrix[0])):
        temp_col = []
        for col_idx in range(len(matrix)):
            temp_col.append(matrix[col_idx][row_idx])
        transposed_matrix.append(temp_col)
    return transposed_matrix


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transpose([[1, 2, 3], [4, 5, 6]]))
