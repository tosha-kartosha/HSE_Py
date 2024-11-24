"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        flag = False
        tek_len = 1
        minLen = 0
        left_ptr = 0
        right_ptr = 0
        tek_sum = nums[left_ptr]
        while (left_ptr <= len(nums) - 1) and (right_ptr < len(nums)):
            if tek_sum >= target:
                if flag:
                    minLen = min(minLen, tek_len)
                else:
                    minLen = tek_len
                    flag = True
                tek_sum -= nums[left_ptr]
                left_ptr += 1
                tek_len -= 1
            else:
                right_ptr += 1
                if right_ptr < len(nums):
                    tek_sum += nums[right_ptr]
                    tek_len += 1
        return minLen
