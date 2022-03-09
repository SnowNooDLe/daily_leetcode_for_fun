"""
82. Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.


Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """Runtime 44ms, Memory 13.9MB"""

    # Create a dummy ListNode as we are going to extend this node
    dummy = ListNode(0, head)
    # clone it (but share memory) to modify dummy's next linked lists
    temp = dummy

    while head:
        # see if next and one after is same
        if head.next and head.val == head.next.val:
            # and if so, we keep checking until cur val and next val are not same
            while head.next and head.val == head.next.val:
                head = head.next
            # value is no longer same between cur and next, set the next node to temp's next
            temp.next = head.next
        else:
            # value is not same so we can safely add
            temp = temp.next

        # mode to next head
        head = head.next

    # Because dummy val is 0, so we return linked list from the next node
    return dummy.next


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(3)
    e = ListNode(4)
    f = ListNode(4)
    g = ListNode(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    answer = delete_duplicates(a)

    while answer:
        print(answer.val)
        answer = answer.next
