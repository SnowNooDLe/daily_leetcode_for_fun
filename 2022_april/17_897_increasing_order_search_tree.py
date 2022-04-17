"""
897. Increasing Order Search Tree

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the
root of the tree, and every node has no left child and only one right child.

images from https://leetcode.com/problems/increasing-order-search-tree/

Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:
Input: root = [5,1,7]
Output: [1,null,5,null,7]
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

    def increasingBST(self, root: TreeNode) -> TreeNode:
        """Runtime 39ms, Memory 13.9MB"""
        # To get all the values within the tree
        self.get_values(root)
        # Sort it
        self.values.sort()

        answer = TreeNode(self.values[0])
        temp = answer

        for value in self.values[1:]:
            temp.right = TreeNode(value)
            temp = temp.right

        return answer
