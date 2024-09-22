"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-valid-parentheses/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count_open = 0
        stack = [0] * (100)
        for j in range(100):
            stack[j] = [0] * 2
        obstacle = 0
        size = -1
        tek_max = ans_max = 0
        for i in range(len(s)):
            if s[i] == ")" and count_open == 0:
                tek_max = 0
                count_open = 0
                size = -1
                obstacle = 0
            elif s[i] == ")":
                tek_max += 2
                count_open -= 1
                if obstacle > 0:
                    obstacle -= 1
                while size >= 0 and obstacle < stack[size][1]:
                    tek_max += stack[size][0]
                    size -= 1
                ans_max = max(ans_max, tek_max)
            elif s[i] == "(":
                count_open += 1
                if tek_max != 0:
                    size += 1
                    stack[size][0] = tek_max
                    stack[size][1] = obstacle + 1
                    tek_max = 0
                if size >= 0:
                    obstacle += 1
        return ans_max
