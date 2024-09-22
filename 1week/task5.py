"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/wildcard-matching/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(s) != 0 and len(p) == 0:
            return False
        elif len(s) == 0 and len(p) != 0 and p.count("*") != len(p):
            return False
        elif len(s) == 0 and len(p) != 0 and p.count("*") == len(p):
            return True
        count_star = 0
        arr = [[0] * len(s) for i in range(len(p))]
        for i in range(len(p)):
            if i != 0:
                if p[i] == "*" and arr[i - 1][0] == 1:
                    arr[i][0] = 1
                    count_star += 1
                if ((p[i] == "?" or (p[i] == s[0]))) and (count_star == i):
                    arr[i][0] = 1
            elif i == 0 and p[0] == "*":
                arr[0][0] = 1
                count_star += 1
            elif i == 0 and (p[0] == "?" or p[0] == s[0]):
                arr[0][0] = 1
            for j in range(1, len(s)):
                if i == 0 and (s[0] == p[0] or p[0] == "?"):
                    arr[0][0] = 1
                elif i == 0 and p[0] == "*":
                    arr[0][j] = 1
                elif i != 0 and j != 0:
                    if p[i] == "*":
                        arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
                    elif s[j] == p[i] or p[i] == "?":
                        arr[i][j] = arr[i - 1][j - 1]
        return True if arr[len(p) - 1][len(s) - 1] == 1 else False
