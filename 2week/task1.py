"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/zigzag-conversion/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ""
        step1 = 2 * (numRows - 1)
        step2 = 0
        ind, row = 0, 0
        flag = True
        if numRows == 1 or len(s) < numRows:
            return s
        else:
            while step1 >= 0 and row < numRows:
                answer += s[ind]
                if row == 0:
                    ind += step1
                elif row == numRows - 1:
                    ind += step2
                else:
                    if flag:
                        ind += step1
                        flag = False
                    else:
                        ind += step2
                        flag = True
                if ind >= len(s):
                    row += 1
                    ind = row
                    step1 -= 2
                    step2 += 2
                    flag = True
            return answer
