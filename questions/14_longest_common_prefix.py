"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """Runtime 42 ms, Memory 14.3 MB"""
    prefix = ""

    for i in range(len(min(strs, key=len))):
        temp_pre = ""
        for item in strs:
            if temp_pre == "":
                temp_pre = item[i]
            else:
                if item[i] == temp_pre:
                    continue
                else:
                    return prefix
        prefix += temp_pre

    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
