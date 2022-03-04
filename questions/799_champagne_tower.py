"""
799. Champagne Tower

Description for this question is better with image
https://leetcode.com/problems/champagne-tower/

Example 1:
Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:
Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

Example 3:
Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000
"""


def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
    """Runtime 118ms, Memory 13.9MB"""
    # Pre-compute the cups based on the given row
    cups = [[0] * x for x in range(1, query_row + 2)]
    # Top glass, start with the number of poured one
    cups[0][0] = poured

    for row_idx in range(query_row):
        for cup_idx in range(len(cups[row_idx])):
            # Anything tha gets overflowed, minus its cup as 1.0 is full cup, split two ways, divide by 2
            over_flow = (cups[row_idx][cup_idx] - 1) / 2.0
            # if there is any over flow
            if over_flow > 0:
                # split the overflows amount to bottom left and right cups
                cups[row_idx + 1][cup_idx] += over_flow
                cups[row_idx + 1][cup_idx + 1] += over_flow

    # If that cup's value is smaller than 1.0 means its not full so return whatever inside
    # Else, means the cup is full, return 1.0
    return cups[query_row][query_glass] if cups[query_row][query_glass] <= 1.0 else 1.0


print(champagne_tower(1, 1, 1))
print(champagne_tower(2, 1, 1))
print(champagne_tower(100000009, 33, 17))
