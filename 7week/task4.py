"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/fruit-into-baskets/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1
        right_ptr = 1
        tek_ans = 2
        fruit1 = fruits[0]
        fruit1_x = 0
        fruit2_x = 0
        right_ptr = 1
        while right_ptr < len(fruits) and fruit1 == fruits[right_ptr]:
            right_ptr += 1
            fruit1_x += 1
            tek_ans += 1
        if right_ptr == len(fruits):
            return len(fruits)
        fruit2_x = right_ptr
        fruit2 = fruits[right_ptr]
        max_ans = tek_ans
        right_ptr += 1
        while right_ptr < len(fruits):
            max_ans = max(max_ans, tek_ans)
            if fruits[right_ptr] == fruit1:
                fruit1_x = right_ptr
                tek_ans += 1
            elif fruits[right_ptr] == fruit2:
                fruit2_x = right_ptr
                tek_ans += 1
            else:
                if fruit1_x < fruit2_x:
                    tek_ans = fruit2_x - fruit1_x + 1
                    fruit1 = fruit2
                    fruit2 = fruits[right_ptr]
                    fruit1_x = fruit2_x
                    fruit2_x = right_ptr
                else:
                    tek_ans = fruit1_x - fruit2_x + 1
                    fruit2 = fruits[right_ptr]
                    fruit2_x = right_ptr
            max_ans = max(max_ans, tek_ans)
            right_ptr += 1
        return max_ans
