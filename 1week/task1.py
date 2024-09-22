"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        answer = 0
        sign = False
        if len(s) == 0:
            return answer
        for elem in range(len(s)):
            if s[elem] != " ":
                break
        if s[elem] == "-":
            sign = True
            s = s[elem + 1 :]
        elif s[elem] == "+":
            s = s[elem + 1 :]
        else:
            s = s[elem:]
        for elem in s:
            if elem not in "0123456789":
                break
            else:
                if sign:
                    if answer * 10 + int(elem) > 2**31:
                        answer = 2**31
                        break
                else:
                    if answer * 10 + int(elem) > (2**31) - 1:
                        answer = (2**31) - 1
                        break
                answer = answer * 10 + int(elem)
        if sign:
            answer *= -1
        return answer
