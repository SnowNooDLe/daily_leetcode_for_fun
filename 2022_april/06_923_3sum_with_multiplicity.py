"""
923. 3Sum With Multiplicity

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.


Example 1:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
"""
from typing import List
import collections


def threeSumMulti(arr: List[int], target: int) -> int:
    tracker = collections.Counter(arr)
    answer = 0
    for i in tracker:
        for j in tracker:
            k = target - i - j
            if k in tracker:
                i_occurrence = tracker[i]
                j_occurrence = tracker[j]
                k_occurrence = tracker[k]

                if i == j == k:
                    answer += (
                        i_occurrence * (i_occurrence - 1) * (i_occurrence - 2)
                    ) / 6
                elif i == j and i != k:
                    answer += (i_occurrence * (i_occurrence - 1)) / 2 * k_occurrence
                elif i < j < k:
                    answer += i_occurrence * j_occurrence * k_occurrence

            answer %= 10 ** 9 - 7
    return int(answer)


print(threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
print(threeSumMulti([1, 1, 2, 2, 2, 2], 5))
