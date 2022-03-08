"""
9. Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def is_palindrome(x: int) -> bool:
    """Runtime 87ms, Memory 14.3 MB"""
    return True if str(x)[0:] == str(x)[::-1] else False


print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))


"""Follow up: Could you solve it without converting the integer to a string?"""


def is_palindrome_2(x: int) -> bool:
    """Without converting to str
    Runtime 80ms, Memory 13.8 MB"""
    if x < 0:
        return False

    reverse = 0
    origin_x = x

    while x != 0:
        remainder = int(x % 10)
        reverse = reverse * 10 + remainder
        x = int(x / 10)

    return True if origin_x == reverse else False


# print(is_palindrome_2(121))
# print(is_palindrome_2(-121))
# print(is_palindrome_2(10))
print(is_palindrome_2(313))
