"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s: str) -> int:
    """Runtime 80ms, Memory 14.1MB"""
    if len(s) == 0:
        return 0
    subs = ""
    longest_subs = ""
    for i in range(0, len(s)):
        if s[i] in subs:
            subs = subs[subs.index(s[i]) + 1 :]
        subs += s[i]

        if len(subs) > len(longest_subs):
            longest_subs = subs

    return len(longest_subs)


# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("bbbbb"))
# print(lengthOfLongestSubstring("pwwkew"))
# print(lengthOfLongestSubstring("dvdf"))
# print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("aabaab!bb"))
