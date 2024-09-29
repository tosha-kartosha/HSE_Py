"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        tek_len = 0
        st = 0
        tek_alf = {}
        for i in range(len(s)):
            if s[i] not in tek_alf or (s[i] in tek_alf and tek_alf[s[i]] < st):
                tek_alf[s[i]] = i
                tek_len += 1
            else:
                tek_len = i - tek_alf[s[i]]
                st = tek_alf[s[i]] + 1
                tek_alf[s[i]] = i
            max_len = max(max_len, tek_len)
        return max_len
