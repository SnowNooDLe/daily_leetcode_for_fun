"""
61. Rotate List - more info can be found here https://leetcode.com/problems/rotate-list/

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Runtime 83ms, Memory 13.9MB"""
    visited = []
    length = 0

    # Record all the possible values from linked list
    while head:
        visited.append(head.val)
        length += 1
        head = head.next

    # Create a new list based by moving index by k and modulo by size of to keep them in order
    dummy_list = [0] * length
    for idx, value in enumerate(visited):
        dummy_list[(idx + k) % length] = value

    # Based on the shifted values, create a linked list
    final = ListNode(0, None)
    temp = final

    for value in dummy_list:
        temp.next = ListNode(value, None)
        temp = temp.next

    return final.next
