"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        max_value = 0
        all_words = {}
        for elem in strs:
            sort_letter = "".join(sorted(elem))
            if sort_letter in all_words:
                answer[all_words[sort_letter]].append(elem)
            else:
                all_words[sort_letter] = max_value
                answer.append([elem])
                max_value += 1
        return answer
