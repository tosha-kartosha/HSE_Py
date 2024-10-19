"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        without_dubl = set(nums)
        max_count = 0
        tek_count = 0
        for elem in nums:
            if elem - 1 not in without_dubl:
                tek_count = elem + 1
                while tek_count in without_dubl:
                    tek_count += 1
                max_count = max(max_count, tek_count - elem)
        return max_count
