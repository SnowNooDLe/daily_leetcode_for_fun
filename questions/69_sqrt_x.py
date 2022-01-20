"""
69. Sqrt(x)

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.


Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""


def my_sqrt(x: int) -> int:
    """Runtime 4256ms, Memory 14.1MB"""
    if x == 1:
        return x

    for i in range(1, x + 1):
        if i * i == x:
            return i
        elif i * i > x:
            return i - 1


print(my_sqrt(4))
print(my_sqrt(8))
