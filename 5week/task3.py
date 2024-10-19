"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/set-matrix-zeroes/description/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_znach = False
        col_znach = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_znach = True
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                row_znach = True
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        for j in range(len(matrix[0])):
            if row_znach:
                matrix[0][j] = 0
        for i in range(len(matrix)):
            if col_znach:
                matrix[i][0] = 0
