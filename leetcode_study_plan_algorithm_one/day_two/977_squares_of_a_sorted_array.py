"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    """Runtime 317ms, Memory 16.2MB"""
    squared = [num * num for num in nums]
    squared.sort()
    return squared


print(sorted_squares([-4, -1, 0, 3, 10]))
print(sorted_squares([-7, -3, 2, 3, 11]))

"""
Follow up: Squaring each element and sorting the new array is very trivial.
Could you find an O(n) solution using a different approach?
"""
