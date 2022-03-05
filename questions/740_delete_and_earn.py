"""
740. Delete and Earn

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.


Example 1:
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
"""
from typing import List
from collections import defaultdict


def delete_and_earn(nums: List[int]) -> int:
    """Runtime 83ms, Memory 14.1 MB
    Got some help to get an idea from the following clip
    https://youtu.be/7FCemBxvGw0
    """
    points = defaultdict(int)
    # Count the number of duplicate integer which ends up a score
    for num in nums:
        points[num] += 1
    # To remove duplication and sort array
    nums = sorted(list(set(nums)))

    earn1 = 0
    earn2 = 0
    for idx in range(len(nums)):
        # As there might be more than one element occurred, multiply them to get total score
        cur_earn = nums[idx] * points[nums[idx]]
        # If the current index's value is adjacent to previous (like if current index value is 3, 2 is not valid)
        if idx > 0 and nums[idx] == nums[idx - 1] + 1:
            temp = earn2
            earn2 = max(cur_earn + earn1, earn2)
            earn1 = temp
        # current and previous are not adjacent, can use both
        else:
            temp = earn2
            earn2 = cur_earn + earn2
            earn1 = temp

    return earn2


print(delete_and_earn([3, 4, 2]))
print(delete_and_earn([2, 2, 3, 3, 3, 4]))
