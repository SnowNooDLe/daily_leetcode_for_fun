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
    """As specified, each input would have EXACTLY ONE SOLUTION and not use the SAME ELEMENT TWICE
    Hence, start putting the difference between target and each value from the given list

    For instance, with the first example:
    The first value is 2 but 2 is not in the vals, add 9-2 = 7, now vals = [7]
    The second value is 7 and 7 is in vals. Hence, we pair the index of current value from vals and nums
    vals = [7], vals.index(value=7) = 0 and index which is 1 as it's the second element of the nums
    as we go over the nums list, we create vals which is a temporary list, so the indexes are matching.

    With the second example:
    The first value is 3 but 3 is not in the vals, add 6-3=3, now vals = [3]
    The second value is 2 but 2 is also not in the vals, add 6-2=4, now vals = [3,4]
    The third value is 4 and 4 is in the vals, then we return as
    vals = [3,4], vals.index(value=4) = 1 and index which is 2 => [1,2]

    """
    vals = []
    for index, value in enumerate(nums):
        if value in vals:
            return [vals.index(value), index]
        vals.append(target - value)


print(two_sum_2([2, 7, 11, 15], 9))
print(two_sum_2([3, 2, 4], 6))
print(two_sum_2([3, 3], 6))
