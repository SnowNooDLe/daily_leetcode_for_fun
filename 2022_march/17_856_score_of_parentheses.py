"""
856. Score of Parentheses

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:
Input: s = "()"
Output: 1

Example 2:
Input: s = "(())"
Output: 2

Example 3:
Input: s = "()()"
Output: 2
"""


def scoreOfParentheses(s: str) -> int:
    """
    Watched the following video as a reference
    https://www.youtube.com/watch?v=jfmJusJ0qKM
    """
    trace_stack = []
    score = 0
    for char in s:
        if char == "(":
            # Open bracket means it starts again from here, so add score
            trace_stack.append(score)
            # regardless of the previous score, reset it to 0
            score = 0
        else:
            # Closing bracket is the time we calculate the score
            score = trace_stack.pop() + max(score * 2, 1)

    return score


print(scoreOfParentheses("()"))
print(scoreOfParentheses("(())"))
print(scoreOfParentheses("()()"))
print(scoreOfParentheses("(()(()))"))
