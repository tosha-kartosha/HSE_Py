"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/find-bottom-left-tree-value/description/?envType=problem-list-v2&envId=binary-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        arr = [root]
        while arr:
            ans = arr[0].val
            for _ in range(len(arr)):
                tek = arr.pop(0)
                if tek.left:
                    arr.append(tek.left)
                if tek.right:
                    arr.append(tek.right)
        return ans
