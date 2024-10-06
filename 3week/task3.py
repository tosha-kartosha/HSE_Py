"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/rotate-image/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for k in range(len(matrix) // 2):
            for i in range(k, len(matrix) - k - 1):
                elem = matrix[k][i]
                tek_x = k
                tek_y = i
                for _ in range(4):
                    new_x = tek_y
                    new_y = len(matrix) - 1 - tek_x
                    matrix[new_x][new_y], elem = elem, matrix[new_x][new_y]
                    tek_x = new_x
                    tek_y = new_y
