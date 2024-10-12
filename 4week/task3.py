"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/jump-game/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_elem = nums[0]
        i = 1
        while i < len(nums) - 1 and i <= max_elem:
            max_elem = max(max_elem, i + nums[i])
            i += 1
        if max_elem >= len(nums) - 1:
            return True
        else:
            return False
