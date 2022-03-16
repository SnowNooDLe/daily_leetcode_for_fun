"""
946. Validate Stack Sequences

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.


Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
"""
from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    """Runtime 97ms, Memory 14.2MB"""
    trace_stack = []
    i = 0
    for val in pushed:
        # Staring to push itme to temp stack to check with popped
        trace_stack.append(val)
        # If the last element from stack is equal to the i index of popped, we pop this item from stack
        # and increase the index i to track the next element from popped list
        while trace_stack and trace_stack[-1] == popped[i]:
            trace_stack.pop()
            i += 1

    # if we managed to eliminate all the elements from stack, it means the given popped list is a valid
    # array of popped, else, some order is not right
    return True if len(trace_stack) == 0 else False


print(validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
print(validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
