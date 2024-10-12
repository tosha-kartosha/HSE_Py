"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/spiral-matrix/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        amount = m * n
        answer = []
        x, y = 0, 0
        while len(answer) != amount:
            for i in range(4):
                if i == 0:
                    for j in range(y, n):
                        answer += [matrix[x][j]]
                    if len(answer) == amount:
                        return answer
                elif i == 1:
                    for j in range(x + 1, m):
                        answer += [matrix[j][n - 1]]
                    if len(answer) == amount:
                        return answer
                elif i == 2:
                    for j in range(n - 2, y - 1, -1):
                        answer += [matrix[m - 1][j]]
                    n -= 1
                else:
                    for j in range(m - 2, x, -1):
                        answer += [matrix[j][y]]
                    if len(answer) == amount:
                        return answer
                    x += 1
                    y += 1
                    m -= 1
        return answer
