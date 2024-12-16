"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root in (None, p, q):
            return root
        left_child = self.lowestCommonAncestor(root.left, p, q)
        right_child = self.lowestCommonAncestor(root.right, p, q)
        return (
            right_child
            if left_child is None
            else left_child if right_child is None else root
        )
