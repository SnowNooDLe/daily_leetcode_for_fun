"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # Getting a min depth for the left subtree
        l = self.minDepth(root.left)
        # Getting a min depth for the right subtree
        r = self.minDepth(root.right)

        # left child does not exist, consider the depth returned by the right subtree
        if root.left is None:
            return 1 + r

        # right child does not exist, consider the depth returned by the left subtree
        if root.right is None:
            return 1 + l

        # Otherwise compare between left and right
        return min(l, r) + 1
