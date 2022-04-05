"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""
from typing import List


def maxArea(height: List[int]) -> int:
    """Runtime 1027ms, Memory 27.5MB"""
    # Two pointers approach from the left and right
    left = 0
    right = len(height) - 1
    area = 0
    while left < right:
        # We only care the actual area so use the max to trace
        # x axis will be easy part, right - left
        # height is whichever that was lower so use the minimum
        area = max(area, (right - left) * min(height[left], height[right]))
        # Which ever the lower height, we move to the next one we only care the smaller height
        # E.g., left's height 7, right's height 9, 9 doesn't mean we can fill up by 9 as left one is only 7
        # won't be able to keep over 7
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
print(maxArea([2, 3, 4, 5, 18, 17, 6]))
