"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)
        p = "".join(sorted(p))
        ans = []
        for i in range(len_s - len_p + 1):
            if "".join(sorted(s[i : i + len_p])) == p:
                ans.append(i)
        return ans
