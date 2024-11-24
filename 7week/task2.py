"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        raznost = []
        res = [0] * (len(nums) - 2)
        answer = 0
        tek_ans = 0
        for i in range(1, len(nums)):
            raznost.append(nums[i] - nums[i - 1])
        for i in range(1, len(raznost)):
            if raznost[i] == raznost[i - 1]:
                res[i - 1] += 1
        for i in range(len(res)):
            if res[i] == 0 and tek_ans != 0:
                answer += (1 + tek_ans) * tek_ans // 2
                tek_ans = 0
            elif res[i] != 0:
                tek_ans += 1
        if tek_ans != 0:
            answer += (1 + tek_ans) * tek_ans // 2
        return answer
