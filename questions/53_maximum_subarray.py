"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""
from typing import List
from itertools import combinations


def max_sub_array(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    all_subarrays = [
        nums[start : end + 1] for start, end in combinations(range(len(nums)), 2)
    ]
    for num in nums:
        all_subarrays.append([num])

    temp_sum = -10000
    for subarray in all_subarrays:
        if sum(subarray) > temp_sum:
            temp_sum = sum(subarray)

    return temp_sum


print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sub_array([1]))
print(max_sub_array([5, 4, -1, 7, 8]))


"""Better approach due to memory issue
Reference: https://leetcode.com/problems/maximum-subarray/discuss/1680930/Python-Simple-Solution-O(n)-time-explained
"""


def max_sub_array_2(nums: List[int]) -> int:
    """Runtime 756ms, Memory 28.8MB"""
    cur_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        cur_val = nums[i]
        cur_sum = max(cur_val, cur_sum + cur_val)
        max_sum = max(cur_sum, max_sum)

    return max_sum


print(max_sub_array_2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sub_array_2([1]))
print(max_sub_array_2([5, 4, -1, 7, 8]))
