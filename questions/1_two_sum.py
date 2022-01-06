"""1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2.
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3.
Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


def two_sum(nums: List[int], target: int):
    """Runtime 3780ms, Memory 14.9 MB"""
    for first_index, first_value in enumerate(nums):
        for second_index, second_value in enumerate(nums[first_index + 1:]):
            if first_value + second_value == target:
                return [first_index, first_index + second_index + 1]


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))


"""Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
To achieve this, I guess we have to remove one of the for loops
"""


def two_sum_2(nums: List[int], target: int):
    """Runtime 525ms, Memory 15.1 MB"""
    vals = []
    for index, value in enumerate(nums):
        if value in vals:
            return [vals.index(value), index]
        vals.append(target - value)


print(two_sum_2([2, 7, 11, 15], 9))
print(two_sum_2([3, 2, 4], 6))
print(two_sum_2([3, 3], 6))
