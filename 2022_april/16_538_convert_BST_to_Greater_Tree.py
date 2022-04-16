"""
538. Convert BST to Greater Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

images from https://leetcode.com/problems/convert-bst-to-greater-tree/

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]
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
        self.is_sorted = False

    def get_values(self, root: Optional[TreeNode]):
        if root is None:
            return None

        self.values.append(root.val)
        root.left = self.get_values(root.left)
        root.right = self.get_values(root.right)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # To get all the values within the tree
        if not self.is_sorted:
            self.get_values(root)
            # Sort it
            self.values.sort()
            self.is_sorted = True

        # Replace it
        if root is None:
            return None

        index = self.values.index(root.val)
        root.val = sum(self.values[index:])

        root.left = self.convertBST(root.left)
        root.right = self.convertBST(root.right)

        return root
