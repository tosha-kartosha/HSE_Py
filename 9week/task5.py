"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=problem-list-v2&envId=binary-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def DFS(node, current_number):
            if not node:
                return 0

            current_number += str(node.val)

            if not node.left and not node.right:
                return int(current_number)

            left_sum = DFS(node.left, str(current_number))
            right_sum = DFS(node.right, str(current_number))

            return left_sum + right_sum

        return DFS(root, "")
