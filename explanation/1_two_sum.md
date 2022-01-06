# 1. [Two Sum](https://leetcode.com/problems/two-sum/)

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

## Better solution

As specified, each input would have EXACTLY ONE SOLUTION and not use the SAME ELEMENT TWICE
Hence, start putting the difference between target and each value from the given list

For instance, with the first example:

- The first `value` is 2 but 2 is not in the `vals`, add 9-2 = 7, now `vals = [7]`
- The second `value` is 7 and 7 is in `vals`. Hence, we pair the index of current value from vals and nums
  `vals = [7], vals.index(value=7) = 0` and `index` which is 1 as it's the second element of the nums.
- As we go over the nums list, we create vals which is a temporary list, so the indexes are matching.

With the second example:

- The first `value` is 3 but 3 is not in the `vals`, add 6-3=3, now `vals = [3]`
- The second `value` is 2 but 2 is also not in the `vals`, add 6-2=4, now `vals = [3,4]`
- The third `value` is 4 and 4 is in the `vals`, then we return as
  `vals = [3,4], vals.index(value=4) = 1` and index which is 2 => `[1,2]`

```python
def two_sum_2(nums: List[int], target: int):
    vals = []
    for index, value in enumerate(nums):
        if value in vals:
            return [vals.index(value), index]
        vals.append(target - value)

# Example code
print(two_sum_2([2, 7, 11, 15], 9))
print(two_sum_2([3, 2, 4], 6))
print(two_sum_2([3, 3], 6))
```
