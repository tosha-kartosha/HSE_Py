"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/candy/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in range(len(ratings))]
        count_des = 0
        all_candies = 0
        IsRising = False
        prev_for_max = 0
        if len(ratings) == 1:
            return 1
        if ratings[0] <= ratings[1]:
            all_candies = 1
        else:
            count_des = 1
        for i in range(1, len(ratings) - 1):
            if ratings[i] > ratings[i - 1]:
                if ratings[i] > ratings[i + 1]:
                    count_des = 1
                    IsRising = True
                    prev_for_max = candies[i - 1] + 1
                else:
                    all_candies += candies[i - 1] + 1
                    candies[i] = candies[i - 1] + 1
            elif ratings[i - 1] == ratings[i]:
                if ratings[i] > ratings[i + 1]:
                    count_des = 1
                else:
                    all_candies += 1
            else:
                if ratings[i] > ratings[i + 1]:
                    count_des += 1
                else:
                    count_des += 1
                    all_candies += (1 + count_des) * count_des // 2
                    if IsRising:
                        if prev_for_max > count_des:
                            all_candies = all_candies - count_des + prev_for_max
                    IsRising = False
                    count_des = 0
                    prev_for_max = 0
            print(all_candies)
        if ratings[-1] == ratings[-2]:
            return all_candies + 1
        elif ratings[-1] > ratings[-2]:
            return all_candies + candies[-2] + 1
        else:
            count_des += 1
            all_candies += (1 + count_des) * count_des // 2
            if IsRising:
                if prev_for_max > count_des:
                    all_candies = all_candies - count_des + prev_for_max
            IsRising = False
            count_des = 0
            prev_for_max = 0
            return all_candies
