"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


def is_palindrome(s: str) -> bool:
    """Runtime 49ms, Memory 14.4MB"""
    # First, lower all the characters in the given string
    s = s.lower()
    sanitized_str = ""
    # Then, remove any non-alphanumeric characters
    for char in s:
        if 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57:
            sanitized_str += char

    # Finally, compare if original and reversed string are same
    return sanitized_str == sanitized_str[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(" "))
print(is_palindrome(""))
print(is_palindrome("0P"))
