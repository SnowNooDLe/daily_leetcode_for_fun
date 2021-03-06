"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Runtime 1464ms, Memory 17.6MB not the best approach I reckon"""
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        else:
            return None  # if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
        return head


# if __name__ == "__main__":
#     a = ListNode(3)
#     b = ListNode(2)
#     c = ListNode(0)
#     d = ListNode(-4)
#
#     a.next = b
#     b.next = c
#     c.next = d
#     d.next = b
#     solution = Solution()
#     print(solution.hasCycle(a))
#
# if __name__ == "__main__":
#     a = ListNode(1)
#     b = ListNode(2)
#
#     a.next = b
#     solution = Solution()
#     print(solution.hasCycle(a))

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print("start")
    b = int(input(""))

    while b not in a:
        break
        print("not in")
        b = int(input(""))
    else:
        print("wtf")
    print("end")
