"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""
from typing import List


def move_zeroes(nums: List[int]) -> None:
    """Runtime 241ms, Memory 15.6MB"""
    size = len(nums)
    i = 0
    while i < size:
        if nums[i] == 0:
            nums.append(nums.pop(i))
            size -= 1
        else:
            i += 1

    print(nums)


print(move_zeroes([0, 0, 1]))

"""
Follow up: Could you minimize the total number of operations done?
"""
