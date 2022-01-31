"""
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
"""


def reverse_words(s: str) -> str:
    """Runtime 43ms, Memory 14.7MB"""
    return " ".join([item[::-1] for item in s.split()])


print(reverse_words("Let's take LeetCode contest"))
print(reverse_words("God Ding"))
