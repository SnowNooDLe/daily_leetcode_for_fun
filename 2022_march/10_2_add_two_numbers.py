"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Runtime 142ms, Memory 13.9MB"""
    # l1 is none then return l2
    if l1 is None:
        return l2

    # l2 is none then return l1
    if l2 is None:
        return l1

    # Create a new node so we can return from the beginning
    temp = ListNode(0, None)
    dummy = temp
    previous_over_ten = False

    # Go through each node to calculate
    while l1 and l2:
        sum = l1.val + l2.val if not previous_over_ten else l1.val + l2.val + 1

        # To determine whether previous was higher than 10
        previous_over_ten = True if sum >= 10 else False

        dummy.next = ListNode(sum % 10, None)

        # Move to the next node
        dummy = dummy.next
        l1 = l1.next
        l2 = l2.next

    # Last two nodes' sum was not higher than ten
    if not previous_over_ten:
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
    # Previous sum was higher than ten
    else:
        if l1:
            while l1:
                sum = l1.val + 1 if previous_over_ten else l1.val

                previous_over_ten = True if sum >= 10 else False

                dummy.next = ListNode(sum % 10, None)

                dummy = dummy.next
                l1 = l1.next

        else:
            while l2:
                sum = l2.val + 1 if previous_over_ten else l2.val

                previous_over_ten = True if sum >= 10 else False

                dummy.next = ListNode(sum % 10, None)

                dummy = dummy.next
                l2 = l2.next

        if previous_over_ten:
            dummy.next = ListNode(1, None)

    return temp.next
