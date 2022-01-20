"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""


def add_binary(a: str, b: str) -> str:
    """Runtime 53ms, Memory 14.4MB"""
    if a == "":
        return b
    elif b == "":
        return a

    # int(str, 2) converts the given str binary code to int
    # Then convert back the summed value to binary with {0:b}
    return "{0:b}".format(int(a, 2) + int(b, 2))


print(add_binary("11", "1"))
print(add_binary("1010", "1011"))
