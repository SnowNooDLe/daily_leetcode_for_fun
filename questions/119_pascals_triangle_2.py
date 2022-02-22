"""
118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
"""
from typing import List


def getRow(rowIndex: int) -> List[int]:
    """Runtime 32ms, Memory 13.9ms"""
    answers = [[1], [1, 1]]
    if rowIndex < 2:
        return answers[rowIndex]

    # From row 3, some calculation needs to be done
    start_row_index = 2
    """
       1
      1 1
     1 2 1 index 0 and row-1 = 1, middle index = previous row's middle index - 1 + index
    1 3 3 1  
    """
    while start_row_index <= rowIndex:
        new_row = []
        for i in range(start_row_index + 1):
            # Very first and last element is always 1
            if i == 0 or i == start_row_index:
                new_row.append(1)
            else:
                # Add previous row's index - 1 + index's values
                new_row.append(
                    answers[start_row_index - 1][i - 1]
                    + answers[start_row_index - 1][i]
                )
        answers.append(new_row)
        start_row_index += 1

    # Unlike the Pascal's triangle, return the n'th row
    return answers[rowIndex]


print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(3))
