"""
680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.


Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
"""


def validPalindrome(s: str) -> bool:
    """Runtime 106ms, Memory 14.6MB"""
    start = 0
    length = len(s)
    end = length - 1
    # To track number of count
    check_required = False

    while start <= end:
        # We found one element is not matching between
        # left and right side of string
        if s[start] != s[end]:
            check_required = True
            break
        start += 1
        end -= 1

    # If required
    if check_required:
        # Creating a string without an element at the left index
        part_a = s[:start] + s[start + 1 :]
        # Another string without an element at the right index
        part_b = s[:end] + s[end + 1 :]
        # and see if they can be palindrome
        return part_a == part_a[::-1] or part_b == part_b[::-1]
    else:
        # No need to check and they are already palindrome
        return True


print(validPalindrome("aba"))
print(validPalindrome("abca"))
print(validPalindrome("abc"))
print(validPalindrome("deeee"))
print(validPalindrome("tebbem"))
