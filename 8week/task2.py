"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        left_ptr = 0
        right_ptr = 0
        if goal == 0 and nums.count(0) == len(nums):
            return len(nums) * (len(nums) + 1) // 2
        if goal == 0:
            while left_ptr < len(nums) and nums[left_ptr] != 0:
                left_ptr += 1
                right_ptr += 1
            if left_ptr == len(nums):
                return 0
            tek_sum = nums[left_ptr]
            while left_ptr < len(nums):
                ans += 1
                if right_ptr + 1 < len(nums):
                    if tek_sum + nums[right_ptr + 1] == goal:
                        right_ptr += 1
                    else:
                        left_ptr += 1
                        while left_ptr < len(nums) and nums[left_ptr] != 0:
                            left_ptr += 1
                        if left_ptr == len(nums):
                            return ans
                        right_ptr = left_ptr
                        tek_sum = nums[left_ptr]
                else:
                    left_ptr += 1
                    right_ptr = left_ptr
            return ans
        tek_sum = nums[left_ptr]
        while left_ptr < len(nums):
            if tek_sum == goal:
                if nums[right_ptr] == 1:
                    pos_right = right_ptr
                ans += 1
                if right_ptr + 1 < len(nums) and tek_sum + nums[right_ptr + 1] == goal:
                    right_ptr += 1
                    tek_sum += nums[right_ptr]
                else:
                    tek_sum -= nums[left_ptr]
                    left_ptr += 1
                    if tek_sum == goal:
                        right_ptr = pos_right

            elif tek_sum < goal:
                if right_ptr + 1 < len(nums):
                    right_ptr += 1
                    tek_sum += nums[right_ptr]
                else:
                    break
        return ans
