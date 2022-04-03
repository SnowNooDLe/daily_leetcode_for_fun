"""
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.


Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
"""
from typing import List


def nextPermutation(nums: List[int]) -> None:
    """I need to go through this again,
    Check the explanation here
    https://leetcode.com/problems/next-permutation/discuss/1908665/Python-or-Easy-nlogn-solution
    Steps I followed:
    1. Find the latest peak in the array (A peak is an element that is greater that the previous element in the array)
    2. If a peak is not found: it means it is in reverse order we just need to revert the array
    3. If a peak is found: it means we can rearrange the array and build a next permutation
    4. Iterate from the latest peak to the end of the array and find the min value in that subarray that is greater than the previous of the latest peak! This because we want to build the next greater permutation
    5. Swap the min value after the peak and the element previous the peak
    6. Sort the array from the latest_peak to the end of the array

    Time complexity = O(nlogn)
    """
    latest_peak = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            latest_peak = i

    if latest_peak == 0:
        nums.reverse()
        return

    pre_peak = latest_peak - 1
    min_after_peak = latest_peak
    for i in range(latest_peak, len(nums)):
        if nums[i] > nums[pre_peak] and nums[i] < nums[min_after_peak]:
            min_after_peak = i

    temp = nums[pre_peak]
    nums[pre_peak] = nums[min_after_peak]
    nums[min_after_peak] = temp

    nums[latest_peak:] = sorted(nums[latest_peak:])


print(nextPermutation([1, 2, 3]))
print(nextPermutation([3, 2, 1]))
print(nextPermutation([1, 1, 5]))
print(nextPermutation([1, 5, 1]))
print(nextPermutation([5, 1, 1]))
print(nextPermutation([2, 2, 7, 5, 4, 3, 2, 2, 1]))
print(nextPermutation([6, 7, 5, 3, 5, 6, 2, 9, 1, 2, 7, 0, 9]))
