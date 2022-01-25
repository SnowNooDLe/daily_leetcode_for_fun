"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Reference
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Runtime 57ms, Memory 14.2MB"""

    def __init__(self):
        self.result = []

    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            self.result.append(root.val)
            self.print_inorder(root.right)

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        self.print_inorder(root)
        return self.result
