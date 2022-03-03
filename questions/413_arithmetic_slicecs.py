"""
413. Arithmetic Slices

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.


Example 1:
Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:
Input: nums = [1]
Output: 0
"""
from typing import List


def number_of_arithmetic_slices(nums: List[int]) -> int:
    """Runtime 49ms, Memory 14MB"""
    # if it consists of at least three elements
    if len(nums) < 3:
        return 0

    result, count = 0, 0
    """
    E.g., [1,2,3,4,5,6]
    minimum length of subarray is three and lets start from index 2 to check first 3
    1,2,3 these are valid arithmetic with 1 different between two consecutive numbers
    so found 1, we move on to index 4 to check 2,3,4
    and 2,3,4 is also valid with 1 different, however, because we know 23 was valid with 1
    and 23 is also valid with 4, hence 1,2,3,4 is also a valid arithmetic, hence these time, we found 2
    so far, we have 3(result = 3, count = 2), we now check 3,4,5 and again, this is valid and we with same reason, 
    we found 3 as 3,4,5, 2,3,4,5 and 1,2,3,4,5 so now result = 6, count = 3, finally, we check 4,5,6 again, 4,5,6 is 
    valid, and count becomes 4 as 4,5,6 + 3 from [1,2,3,4,5] hence in the end, 6 + 4, total 10 for this example.
    """
    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            count += 1
            result += count
        else:
            count = 0

    return result


print(number_of_arithmetic_slices([1, 2, 3, 4]))
print(number_of_arithmetic_slices([1]))
print(number_of_arithmetic_slices([1, 2, 3, 4, 5, 6]))
