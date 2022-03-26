"""
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.


Example 1:
Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Example 2:
Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859

Example 3:
Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
"""
from typing import List


def twoCitySchedCost(costs: List[List[int]]) -> int:
    total_cost = 0
    # Sort the costs by the difference between cost to a city and cost to b city
    sorted_costs = sorted(costs, key=lambda x: x[0] - x[1])
    for idx in range(len(sorted_costs)):
        if idx < len(sorted_costs) / 2:
            # First half of the sorted_costs mean cheaper to flight to A city
            total_cost += sorted_costs[idx][0]
        else:
            # As we already sent N people(out of 2 N people) to City A, rest goes to City B
            total_cost += sorted_costs[idx][1]

    return total_cost
