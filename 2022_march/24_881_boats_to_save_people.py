"""
881. Boats to Save People

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.


Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
"""
from typing import List


def numRescueBoats(people: List[int], limit: int) -> int:
    """Runtime 792ms, memory 20.9MB"""
    # Two pointer, one starts from the left and another one starts from the right
    start = 0
    end = len(people) - 1
    people = sorted(people)
    counter = 0

    while start <= end:
        # With its constraints, the heaviest one is same or smaller to limit and the lightest is minimum 1
        # Hence, if it is bigger than limit, we can only add the heaviest one.
        if people[start] + people[end] > limit:
            # Once added the heaviest one, move the pointer to the next heaviest one.
            end -= 1
            counter += 1
        # We can ship booth the lightest(left/start index) and the heaviest(right/end index)
        else:
            start += 1
            end -= 1
            counter += 1

    return counter


print(numRescueBoats([1, 2], 3))
print(numRescueBoats([3, 2, 2, 1], 3))
print(numRescueBoats([3, 5, 3, 4], 5))
