"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

images from https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.values = []

    def get_values(self, root: Optional[TreeNode]):
        if root is None:
            return None

        self.values.append(root.val)
        self.get_values(root.left)
        self.get_values(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Runtime 54ms, Memory 18MB"""
        # To get all the values within the tree
        self.get_values(root)
        # Sort it
        self.values.sort()

        return self.values[k - 1]
