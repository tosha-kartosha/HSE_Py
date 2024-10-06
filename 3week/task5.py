"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/trapping-rain-water/?envType=problem-list-v2&envId=array
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left_ptr = 1
        right_ptr = len(height) - 2
        left_amount = height[0]
        right_amount = height[-1]

        while left_ptr <= right_ptr:
            if left_amount <= right_amount:
                if left_amount - height[left_ptr] > 0:
                    answer += left_amount - height[left_ptr]
                left_amount = max(left_amount, height[left_ptr])
                left_ptr += 1
            else:
                if right_amount - height[right_ptr] > 0:
                    answer += right_amount - height[right_ptr]
                right_amount = max(right_amount, height[right_ptr])
                right_ptr -= 1
        return answer
