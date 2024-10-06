"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/valid-sudoku/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] in "123456789":
                    step = j + 1
                    while step < 9:
                        if board[i][j] == board[i][step]:
                            return False
                        step += 1
                    step = i + 1
                    while step < 9:
                        if board[i][j] == board[step][j]:
                            return False
                        step += 1
                    left_x = max([num for num in [0, 3, 6] if num <= i])
                    right_x = min([num for num in [2, 5, 8] if num >= i])
                    left_y = max([num for num in [0, 3, 6] if num <= j])
                    right_y = min([num for num in [2, 5, 8] if num >= j])
                    for cor_x in range(left_x, right_x + 1):
                        for cor_y in range(left_y, right_y + 1):
                            if not (i == cor_x and j == cor_y):
                                if board[i][j] == board[cor_x][cor_y]:
                                    return False
        return True
