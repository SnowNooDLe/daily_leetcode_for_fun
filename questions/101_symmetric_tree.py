"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Runtime 36ms, Memory 14MB"""
        def symmetric_binary_tree(root_1, root_2):
            if not root_1 and not root_2:
                return True

            if root_1 and root_2:
                if root_1.val == root_2.val:
                    return symmetric_binary_tree(
                        root_1.left, root_2.right
                    ) and symmetric_binary_tree(root_1.right, root_2.left)
                else:
                    return False

        return symmetric_binary_tree(root.left, root.right)
