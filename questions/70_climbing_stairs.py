"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


n = 1
output = 1
1. 1 step

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

n = 4
output 5
1. 1 step + 1 step + 1 step + 1 step
2. 1 step + 1 step + 2 step
3. 1 step + 2 step + 1 step
4. 2 step + 1 step + 1 step
5. 2 step + 2 step

n = 5
output 8
1. 1 step + 1 step + 1 step + 1 step + 1 step
2. 1 step + 1 step + 1 step + 2 step
3. 1 step + 1 step + 2 step + 1 step
4. 1 step + 2 step + 1 step + 1 step
5. 2 step + 1 step + 1 step + 1 step
6. 1 step + 2 step + 2 step
7. 2 step + 1 step + 2 step
8. 2 step + 2 step + 1 step


n = 1 => 1
n = 2 => 2
n = 3 => 3
n = 4 => 5
n = 5 => 8

Basically combination of last two, is the current n step's answer...?
"""


def climb_stairs(n: int) -> int:
    """This solution faced Time Limit exceeded issue"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb_stairs(n - 2) + climb_stairs(n - 1)


print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))


def climbStairs(n: int) -> int:
    """Runtime 28ms, Memory 14.3MB"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    numbers = [1] * n
    numbers[0] = 1
    numbers[1] = 2

    for i in range(2, n):
        numbers[i] = numbers[i - 1] + numbers[i - 2]

    return numbers[n - 1]


print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
