"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Runtime 32ms, Memory 13.9MB"""
        i = 0
        dummy = head
        while dummy and dummy.next:
            dummy = dummy.next
            i += 1

        if (i == 0 and n == 1 and not dummy.next) or (i == n - 1):
            return head.next

        source = head
        ix = 0

        while source and source.next:
            if ix == i - n:
                source.next = source.next.next
            else:
                source = source.next
            ix += 1

        return head
