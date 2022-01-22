"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """Runtime 56ms, Memory 14.3"""
    temp = head

    while temp and temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
            continue
        temp = temp.next

    return head
