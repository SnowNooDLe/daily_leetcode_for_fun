"""
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/ for images
Example 1:
Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.
"""
from typing import List


def minDominoRotations(tops: List[int], bottoms: List[int]) -> int:
    """Runtime 2006 ms, Memory 15MB"""
    # To count each domino number's occurrence
    top_occurrence = {num: 0 for num in range(1, 7)}
    bottom_occurrence = {num: 0 for num in range(1, 7)}
    same_top_bottom = {num: 0 for num in range(1, 7)}

    for idx in range(len(tops)):
        top_occurrence[tops[idx]] += 1
        bottom_occurrence[bottoms[idx]] += 1

        # When top and bottom idx value is same
        if tops[idx] == bottoms[idx]:
            same_top_bottom[tops[idx]] += 1

    # Domino number is between 1 and 6, over through each number
    for dom_number in range(1, 7):
        # Number of top + bottom - same occurrence should be equal to number of items in tops(same length to bottom)
        # as this means, when we swap, maximum number of swaps don't go over the total items in tops
        if top_occurrence[dom_number] + bottom_occurrence[dom_number] - same_top_bottom[
            dom_number
        ] == len(tops):
            # As we are looking for the minimum swaps, get the min number between top and bottom, and minus any same
            # number at the same index
            return (
                min(top_occurrence[dom_number], bottom_occurrence[dom_number])
                - same_top_bottom[dom_number]
            )

    # Cannot make either row(top or bottom) to be equal values
    return -1


print(minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
print(minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]))
