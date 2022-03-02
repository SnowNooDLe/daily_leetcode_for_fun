"""
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


def is_subsequence(s: str, t: str) -> bool:
    """Runtime 46ms, Memory 13.8MB"""
    sub_index = []
    previous_index = 0
    for char in s:
        # When the character is found
        if char in t:
            # We get its index from t
            index = t.index(char)
            # add index + previouos index as the string might got shorten by previous character
            sub_index.append(index + previous_index)
            # We only count 1 index + from current character to avoid any duplications
            t = t[index + 1 :]
            # But next char's index should be counted from original string t's index, instead of the shorten one
            previous_index += index
    sorted_index = sorted(sub_index)

    return sub_index == sorted_index and len(sub_index) == len(s)


print(is_subsequence(s="abc", t="ahbgdc"))
print(is_subsequence(s="axc", t="ahbgdc"))
print(is_subsequence(s="aaaaaa", t="bbaaaa"))
print(
    is_subsequence(
        s="twn",
        t="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn",
    )
)
