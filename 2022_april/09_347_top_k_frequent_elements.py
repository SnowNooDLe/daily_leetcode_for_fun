"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""
from typing import List
import collections


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """Runtime 100ms, Memory 18.6MB"""
    counter = collections.Counter(nums)
    return [common[0] for common in counter.most_common(k)]


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([1], 1))
print(topKFrequent([1, 1, 2, 2, 2, 3, 3, 3], 5))
print(topKFrequent([3, 0, 1, 0], 1))
