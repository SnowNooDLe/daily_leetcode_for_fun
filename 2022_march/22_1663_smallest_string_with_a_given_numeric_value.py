"""
1663. Smallest String With A Given Numeric Value

The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.


Example 1:
Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.

Example 2:
Input: n = 5, k = 73
Output: "aaszz"
"""
CONSTANT_NUMERIC = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
}


def getSmallestString(n: int, k: int) -> str:
    """Runtime 770ms, Memory 15.8MB"""
    answer = []
    MAX_NUMERIC_VAL = 26
    # AS we want n number of characters
    while n > 0:
        # Before we add a new element, by hitting here means we needed to add more element,
        # But we can't just use the "z" just because given k is bigger than 26 as if n = 3, k = 27,
        # it must be aay, can't be az as the length of this is only 2 not 3
        # Hence maximum_numeric key for CONSTANT_NUMERIC is total k - n + 1
        # k = total sum of integer, n = number of items, +1 we are going to add one regardless as we will add something
        max_numeric = k - n + 1
        # If its bigger than or equal to 26, we can safely add z
        if max_numeric >= MAX_NUMERIC_VAL:
            answer.append("z")
            k -= MAX_NUMERIC_VAL
        else:
            answer.append(CONSTANT_NUMERIC[max_numeric])
            k -= max_numeric
        # Decrease n by 1 as we managed to add a character
        n -= 1

    return "".join(answer[::-1])


print(getSmallestString(3, 27))
print(getSmallestString(5, 73))
