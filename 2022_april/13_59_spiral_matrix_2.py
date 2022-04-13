"""
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

image from https://leetcode.com/problems/spiral-matrix-ii/
Example 1:

00  01  02
10  11  12
20  21  22


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
"""
from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    """Runtime 34ms, Memory 14MB"""
    num = 1
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    answer = [[0] * n for _ in range(n)]

    while num <= n * n:
        # top section
        for idx in range(left, right + 1):
            answer[top][idx] = num
            num += 1
        top += 1

        # right section
        for idx in range(top, bottom + 1):
            answer[idx][right] = num
            num += 1
        right -= 1

        # bottom section
        for idx in range(right, left - 1, -1):
            answer[bottom][idx] = num
            num += 1
        bottom -= 1

        # left section
        for idx in range(bottom, top - 1, -1):
            answer[idx][left] = num
            num += 1
        left += 1

    return answer


print(generateMatrix(3))
print(generateMatrix(1))
