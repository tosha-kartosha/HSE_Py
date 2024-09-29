"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/regular-expression-matching/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        count_row = len(p) - p.count("*") + 1
        count_column = len(s) + 1
        case_star = False
        step_p = 0
        arr = [[0] * count_column for i in range(count_row)]
        arr[0][0] = 1
        ind_x, ind_p = 1, 0
        while ind_x < count_row:
            ind_y = 0
            if ind_p + 1 < len(p) and p[ind_p + 1] == "*":
                case_star = True
            else:
                case_star = False
            while ind_y < count_column:
                if ind_y == 0:
                    if case_star:
                        arr[ind_x][0] = arr[ind_x - 1][0]
                        step_p = 2
                    else:
                        step_p = 1
                else:
                    if case_star:
                        if p[ind_p] == "." or p[ind_p] == s[ind_y - 1]:
                            arr[ind_x][ind_y] = max(
                                arr[ind_x][ind_y - 1], arr[ind_x - 1][ind_y]
                            )
                        elif p[ind_p] != s[ind_y - 1]:
                            arr[ind_x][ind_y] = arr[ind_x - 1][ind_y]
                    else:
                        if s[ind_y - 1] == p[ind_p] or p[ind_p] == ".":
                            arr[ind_x][ind_y] = arr[ind_x - 1][ind_y - 1]
                ind_y += 1
            ind_x += 1
            ind_p += step_p
        return arr[-1][-1]
