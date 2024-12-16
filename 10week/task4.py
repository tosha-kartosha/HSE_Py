"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/balance-a-binary-search-tree/description/?envType=problem-list-v2&envId=binary-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []

        def Inorder(root):
            if root is None:
                return
            Inorder(root.left)
            arr.append(root.val)
            Inorder(root.right)

        def BST(left, right):
            if left > right:
                return None
            med = (left + right) // 2
            root = TreeNode(arr[med])
            root.left = BST(left, med - 1)
            root.right = BST(med + 1, right)
            return root

        Inorder(root)
        root_upd = BST(0, len(arr) - 1)
        return root_upd
