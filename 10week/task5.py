"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/even-odd-tree/description/?envType=problem-list-v2&envId=binary-tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def levelOrder(root):
            if not root:
                return []
            answer = []
            arr = [root]
            while len(arr) > 0:
                capacity = len(arr)
                cur_level = []
                for _ in range(capacity):
                    tek_elem = arr[0]
                    del arr[0]
                    cur_level += [tek_elem.val]

                    if tek_elem.left:
                        arr += [tek_elem.left]
                    if tek_elem.right:
                        arr += [tek_elem.right]
                answer += [cur_level]
            return answer

        answer = levelOrder(root)
        for i in range(len(answer)):
            flag = True if i % 2 == 0 else False
            for j in range(len(answer[i])):
                print(answer[i][j], flag)
                if flag:
                    if answer[i][j] % 2 == 0:
                        return False
                    if j != 0:
                        if answer[i][j] <= answer[i][j - 1]:
                            return False
                else:
                    if answer[i][j] % 2 != 0:
                        return False
                    if j != 0:
                        if answer[i][j] >= answer[i][j - 1]:
                            return False
        return True
