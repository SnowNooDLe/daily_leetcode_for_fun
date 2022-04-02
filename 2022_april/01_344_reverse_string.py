"""
344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


def reverse_string(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    Runtime 74ms, Memory 18.6MB
    """
    length = len(s)
    for idx in range(length // 2):
        s[idx], s[length - idx - 1] = s[length - idx - 1], s[idx]


print(reverse_string(["h", "e", "l", "l", "o"]))
print(reverse_string(["H", "a", "n", "n", "a", "h"]))
