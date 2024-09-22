"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/count-and-say/?envType=problem-list-v2&envId=string
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        step = 1
        while step != n:
            new_s = ""
            tek_elem = int(s[0])
            count = 1
            for i in range(1, len(s)):
                if tek_elem != int(s[i]):
                    new_s += str(count) + str(tek_elem)
                    count = 1
                    tek_elem = int(s[i])
                else:
                    count += 1
            new_s += str(count) + str(tek_elem)
            s = new_s
            step += 1
        return s
