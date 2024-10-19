"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/majority-element-ii/description/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_dict = {}
        answer = []
        for elem in nums:
            key = str(elem)
            if key in num_dict:
                num_dict[key] += 1
            else:
                num_dict[key] = 1
            if num_dict[key] > len(nums) / 3 and int(key) not in answer:
                answer.append(int(key))
        return answer
