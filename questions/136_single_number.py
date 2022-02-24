"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""
from typing import List


def singleNumber(nums: List[int]) -> int:
    """Runtime 204ms, Memory 16.8MB"""
    answer = {}
    for number in nums:
        if not number in answer:
            answer[number] = 1
        else:
            answer[number] += 1

    return [k for k, v in answer.items() if v == 1][0]


print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1]))
