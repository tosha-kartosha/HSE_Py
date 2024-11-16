"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-erasure-value/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start, end = 0, 0
        arr = []
        tek_sum, ans = 0, 0
        while end < len(nums):
            while start < end and nums[end] in arr:
                arr.remove(nums[start])
                tek_sum -= nums[start]
                start += 1
            arr += [nums[end]]
            tek_sum += nums[end]
            end += 1
            ans = max(ans, tek_sum)
        return ans
