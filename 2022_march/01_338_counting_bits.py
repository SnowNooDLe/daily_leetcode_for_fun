"""
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""
from typing import List


def count_bits(n: int) -> List[int]:
    """Runtime 123 ms, Memory 20.8MB"""
    return [bin(i)[2:].count("1") for i in range(n + 1)]


print(count_bits(2))
print(count_bits(5))
