"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/permutation-in-string/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)
        if ls1 > ls2:
            return False
        left = 0
        right = ls1
        while right <= ls2:
            wind = s2[left:right]
            if sorted(s1) == sorted(wind):
                return True
            left += 1
            right += 1
        return False
