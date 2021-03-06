"""
669. Trim a Binary Search Tree

Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

images from https://leetcode.com/problems/trim-a-binary-search-tree/

Example 1:
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Example 2:
Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    """runtime 58ms ,Memory 16.2MB"""
    if root is None:
        return None
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)

    if low <= root.val <= high:
        return root

    return root.left if root.left is not None else root.right
