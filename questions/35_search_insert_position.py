"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

"""
from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """Runtime 66ms, Memory 15.1MB"""
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
        elif nums[middle] > target:
            end = middle - 1

    return start


print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 2))
print(search_insert([1, 3, 5, 6], 7))
