"""
991. Broken Calculator

There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:

multiply the number on display by 2, or
subtract 1 from the number on display.
Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.


Example 1:
Input: startValue = 2, target = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Example 2:
Input: startValue = 5, target = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.

Example 3:
Input: startValue = 3, target = 10
Output: 3
Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
"""


def brokenCalc(startValue: int, target: int) -> int:
    count = 0
    while startValue < target:
        # We will apply reverse calculation to target
        # Instead of working on startValue
        # Calculator can only do either minus 1 or multiply by 2
        # Hence options are either divide by 2 or plus 1
        if target % 2 == 0:
            target //= 2
        else:
            target += 1
        count += 1
    # As while loop only works if startValue is smaller than target
    # which startValue may not be same as target but bigger
    # Then just minus the difference as this broken calculator can only do
    # minus 1 or multiply by 2
    return count + (startValue - target)
