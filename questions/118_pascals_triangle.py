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


def generate(numRows: int) -> List[List[int]]:
    """Runtime 38ms, Memory 13.8ms"""
    answers = [[1]]
    if numRows == 1:
        return answers

    # If numRows is >= 2, we can safely add the following array
    answers.append([1, 1])

    if numRows == 2:
        return answers

    # From row 3, some calculation needs to be done
    start_row_index = 2
    """
       1
      1 1
     1 2 1 index 0 and row-1 = 1 rest index = previous row's index - 1 + index
    1 3 3 1  
    """
    while start_row_index < numRows:
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

    return answers


print(generate(5))
print(generate(1))
