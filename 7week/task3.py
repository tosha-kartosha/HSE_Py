"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left_ptr = 0
        right_ptr = 0
        answer = 0
        tek_pr = 1
        while right_ptr < len(nums):
            tek_pr *= nums[right_ptr]
            while tek_pr >= k and left_ptr < len(nums):
                tek_pr //= nums[left_ptr]
                left_ptr += 1
            answer += right_ptr - left_ptr + 1
            right_ptr += 1
        if answer < 0:
            return 0
        return answer
