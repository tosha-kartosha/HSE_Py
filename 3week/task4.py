"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/first-missing-positive/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while (
                (nums[i] > 0)
                and (nums[i] <= len(nums))
                and (nums[i] != i + 1)
                and (nums[nums[i] - 1] != nums[i])
            ):
                tmp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[tmp - 1] = tmp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
