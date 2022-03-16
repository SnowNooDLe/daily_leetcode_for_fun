"""1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""


def minRemoveToMakeValid(s: str) -> str:
    """Runtime 133ms, Memory 16MB"""
    trace_stack = []
    s = list(s)
    for idx, char in enumerate(s):
        # We keep tracking the open parentheses as the valid parentheses look like ()
        if char == "(":
            # We need to have index for ( so we can potentially remove if they are not a valid parentheses
            trace_stack.append({"index": idx, "value": char})
        elif char == ")":
            # Never visited ( but ) came, starting with ) is useless so we store "" instead
            if len(trace_stack) == 0:
                # string += "" does not do anything but we still need to reserve the string at a certain index
                # even thought these will be removed
                # Updated version - We now use list so we can replace it
                s[idx] = ""
            else:
                # At least we have something in stack(either ( or )), and if the last one is ( remove it
                # and we can safely add ) as it's a valid parentheses
                if trace_stack[-1]["value"] == "(":
                    trace_stack.pop()

    # Any left open parentheses, as they are not valid, remove them.
    for stack in trace_stack:
        s[stack["index"]] = ""

    # Because answer is currently in a list, join them and remove any empty string
    return "".join(s)


print(minRemoveToMakeValid("lee(t(c)o)de)"))
print(minRemoveToMakeValid("a)b(c)d"))
print(minRemoveToMakeValid("))(("))
print(minRemoveToMakeValid("(a(b(c)d)"))
print(minRemoveToMakeValid("()()"))
