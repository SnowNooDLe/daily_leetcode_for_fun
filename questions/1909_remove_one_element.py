"""
1909. Remove One Element to Make the Array Strictly Increasing

Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).


Example 1:
Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.

Example 2:
Input: nums = [2,3,1,2]
Output: false
Explanation:
[3,1,2] is the result of removing the element at index 0.
[2,1,2] is the result of removing the element at index 1.
[2,3,2] is the result of removing the element at index 2.
[2,3,1] is the result of removing the element at index 3.
No resulting array is strictly increasing, so return false.

Example 3:
Input: nums = [1,1,1]
Output: false
Explanation: The result of removing any element is [1,1].
[1,1] is not strictly increasing, so return false.
"""
from typing import List


def can_be_increasing(nums: List[int]) -> bool:
    """Runtime 654ms, Memory 14MB"""
    is_strict = True
    # Original case, check without removing any element
    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            is_strict = False
            break

    # Original array is already strictly increasing
    if is_strict:
        return True

    # Need to start popping one element

    for i in range(len(nums)):
        temp = nums[:]
        temp.pop(i)
        is_strict = True
        for j in range(1, len(temp)):
            if temp[j - 1] >= temp[j]:
                is_strict = False
                break

        if is_strict:
            return True

    return is_strict


print(can_be_increasing([1, 2, 10, 5, 7]))
print(can_be_increasing([2, 3, 1, 2]))
print(can_be_increasing([1, 1, 1]))
