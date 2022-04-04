"""
1721. Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
photos can be found
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = right = head
        # First, find the kth node from the left
        for i in range(k - 1):
            left = left.next

        # We now need to find the kth node from the right by
        # Moving towards the right
        end_tracker = left
        # But we move two different nodes at the same time
        # end_tracker = left kth node
        # right= from the start
        # By the time end_tracker hits the end, right should be at the right k-th spot
        while end_tracker.next:
            right, end_tracker = right.next, end_tracker.next

        # Swap between left kth and right kth value
        left.val, right.val = right.val, left.val

        return head
