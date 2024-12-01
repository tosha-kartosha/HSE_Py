"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        ans = 0
        len_nums = len(nums)
        first_ptr = 0
        first_sum = 0
        second_sum = 0
        while first_ptr <= len_nums - firstLen:
            first_sum = sum(nums[first_ptr : first_ptr + firstLen])
            second_sum = 0
            second_ptr = 0
            if first_ptr >= secondLen:
                while second_ptr <= first_ptr - secondLen:
                    second_sum = max(
                        second_sum, sum(nums[second_ptr : second_ptr + secondLen])
                    )
                    second_ptr += 1
            if len_nums - (first_ptr + firstLen - 1) >= secondLen:
                second_ptr = first_ptr + firstLen
                while second_ptr + secondLen - 1 < len_nums:
                    second_sum = max(
                        second_sum, sum(nums[second_ptr : second_ptr + secondLen])
                    )
                    second_ptr += 1
            ans = max(ans, first_sum + second_sum)
            first_ptr += 1
        return ans
