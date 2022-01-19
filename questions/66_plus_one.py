"""
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """Runtime 45ms, Memory 14.4MB"""
    temp_val_index = len(digits) - 1
    previous_increment = False

    # For single element
    if len(digits) == 1:
        if digits[0] == 9:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            digits[0] += 1

        return digits

    # More than one element
    for i, digit in enumerate(digits[::-1]):
        if i == 0:
            if digit == 9:
                digits[temp_val_index - i] = 0
                previous_increment = True
            else:
                digits[temp_val_index - i] += 1
                previous_increment = False
        else:
            if previous_increment:
                if digit == 9:
                    digits[temp_val_index - i] = 0
                    previous_increment = True
                else:
                    digits[temp_val_index - i] += 1
                    previous_increment = False

        if i == temp_val_index:
            if previous_increment:
                if digit == 9:
                    digits[temp_val_index - i] = 0
                    digits.insert(0, 1)
                else:
                    digits[temp_val_index - i] += 1
    return digits


print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([9]))
