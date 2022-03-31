"""
410. Split Array Largest Sum

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.


Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9

Example 3:
Input: nums = [1,4,4], m = 3
Output: 4
"""
from typing import List


def split(nums, largestSum):
    pieces = 1
    temp_total = 0

    for num in nums:
        if temp_total + num > largestSum:
            temp_total = num
            pieces += 1
        else:
            temp_total += num

    return pieces


def splitArray(nums: List[int], m: int) -> int:
    """Used the following video as a reference
    https://www.youtube.com/watch?v=8_FivWxrSK0
    """

    maximum, total = 0, 0
    for num in nums:
        maximum = max(maximum, num)
        total += num

    low = maximum
    high = total
    while low < high:
        mid = low + (high - low) // 2
        pieces = split(nums, mid)
        if pieces > m:
            low = mid + 1
        else:
            high = mid

    return low


print(splitArray([7, 2, 5, 10, 8], 2))
print(splitArray([1, 2, 3, 4, 5], 2))
print(splitArray([1, 4, 4], 3))
