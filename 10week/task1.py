"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree
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
        while root:
            if (p.val < root.val) and (q.val < root.val):
                return self.lowestCommonAncestor(root.left, p, q)
            if (p.val > root.val) and (q.val > root.val):
                return self.lowestCommonAncestor(root.right, p, q)
            return root
