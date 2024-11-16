"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        total_sum = sum(cardPoints)
        wind = 0
        slide = len(cardPoints) - k
        for i in range(0, len(cardPoints) - k):
            wind += cardPoints[i]
        max_sum = total_sum - wind
        for i in range(k):
            wind -= cardPoints[i]
            wind += cardPoints[i + slide]
            max_sum = max(max_sum, total_sum - wind)
        return max_sum
