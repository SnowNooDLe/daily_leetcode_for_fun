"""
316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.


Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
"""


def removeDuplicateLetters(s: str) -> str:
    """Runtime 36ms, Memory 14MB"""
    last_seen = {}
    # To record an index of character that was spotted the last
    for idx, char in enumerate(s):
        last_seen[char] = idx

    # We are going to only add to meet the requirements
    results_stack = []
    for idx, char in enumerate(s):
        # We want each character to be occurred only once, so see if its already in the stack
        if char not in results_stack:
            # However, we want it to be "the smallest in lexicographical order" <-
            # I found this as similar to alphabetical order?
            # So the check condition is
            # 1. Some characters are there first (in results_stack)
            # 2. The last element of the stack and see if its higher than current char (in ASCII way)
            # This means that this won't make the results lexicographical, more likely need to remove
            # 3. The last element of the stack last seen index is higher than current index
            # If the last seen index is higher than current index, this character will come up again, so can be safely
            # Removed now
            while (
                results_stack
                and results_stack[-1] > char
                and last_seen[results_stack[-1]] > idx
            ):
                results_stack.pop()
            results_stack.append(char)

    return "".join(results_stack)


print(removeDuplicateLetters("bcabc"))
print(removeDuplicateLetters("cbacdcbc"))

"""
Some extra explanation with example cbacdcbc
input s
c = 0 idx
b = 1 idx
a = 2 idx
c = 3 idx
d = 4 idx
c = 5 idx
b = 6 idx
c = 7 idx
Hence
last_seen = {
    "c": 7,
    "b": 6,
    "a": 2,
    "d": 4,
}
Within the second for loop,
1. cur_index = 0, char = c, stack = [c] nothing in stack, so append it first
2. cur_index = 1, char = b, stack = [b] because last_seen c's index is 7, current index is 1, and c is bigger than b, so pop it
3. cur_index = 2, char = a, stack = [a] because last_seen b's index is 6, current index is 2, and b is bigger than a, so pop it
4. cur_index = 3, char = c, stack = [a,c] because a is not bigger than c, it does not meet the if statement
5. cur_index = 4, char = d, stack = [a,c,d] because c is not bigger than d, it does not meet the if statement
6. cur_index = 5, char = c, stack = [a,c,d] c is already in the stack, no need to check
6. cur_index = 6, char = b, stack = [a,c,d,b] d is bigger than b, so we should've popped it. However, last_seen d's index is 4
and current index is 6, which is smaller than current index so d will never come again. So it does not meet the if statement
7. cur_index = 7, char = c, stack = [a,c,d,b], c is already in the stack, no need to check.
Hence, results is "acdb" with "the smallest in lexicographical order", as we can see, it cannot be 100% alphabetical order
but this is the smallest that contains every character once.
"""
