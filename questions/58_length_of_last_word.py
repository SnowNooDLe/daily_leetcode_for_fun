"""
58. Length of Last Word

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.


Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


def length_of_last_word(s: str) -> int:
    """Runtime 33ms, Memory 14.3MB"""
    if len(s) == 0:
        return 0

    filtered_str = s.split()

    if len(filtered_str) == 0:
        return 0

    return len(filtered_str[-1])


print(length_of_last_word("Hello World"))
print(length_of_last_word("   fly me   to   the moon  "))
print(length_of_last_word("luffy is still joyboy"))
print(length_of_last_word("a"))
