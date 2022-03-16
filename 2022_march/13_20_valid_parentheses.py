"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

First trial
"""
COMBO = {"(": ")", "[": "]", "{": "}"}


def is_valid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    for i in range(0, len(s), 2):
        if s[i] in COMBO.keys():
            if s[i + 1] != COMBO[s[i]]:
                return False
        else:
            return False
    return True


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
# supposed to be true?
print(is_valid("{[]}"))


"""
Second trial with Stack
"""
OPEN = ["(", "[", "{"]
CLOSE = [")", "]", "}"]


def is_valid(s: str) -> bool:
    """Runtime 43ms, Memory 14.4MB"""
    stack = []

    for item in s:
        if len(stack) == 0:
            # When stack is empty, only open brackets can be inserted
            if item in OPEN:
                stack.append(item)
            else:
                return False
        else:
            # Open bracket can go at anytime, as long as it closes at the right time
            if item in OPEN:
                stack.append(item)
            else:
                # item is now close bracket, needs to match with the top item from the stack
                top_item = stack.pop()
                if item != CLOSE[OPEN.index(top_item)]:
                    return False
    return not bool(len(stack))


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
# supposed to be true?
print(is_valid("{[]}"))
print(is_valid("(("))
print(is_valid("))"))
