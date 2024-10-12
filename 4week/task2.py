"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/spiral-matrix-ii/description/
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        amount = n * n
        answer = [[0] * n for _ in range(n)]
        elem = 0
        x, y = 0, 0
        m = n
        while elem != amount:
            for i in range(4):
                if elem == amount:
                    return answer
                if i == 0:
                    for j in range(y, n):
                        elem += 1
                        answer[x][j] = elem
                elif i == 1:
                    for j in range(x + 1, m):
                        elem += 1
                        answer[j][n - 1] = elem
                elif i == 2:
                    for j in range(n - 2, y - 1, -1):
                        elem += 1
                        answer[m - 1][j] = elem
                    n -= 1
                else:
                    for j in range(m - 2, x, -1):
                        elem += 1
                        answer[j][y] = elem
                    x += 1
                    y += 1
                    m -= 1
        return answer
