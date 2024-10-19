"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/repeated-dna-sequences/description/?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash_table = {}
        max_repeat = 0
        if len(s) < 10:
            return []
        for i in range(0, len(s) - 9):
            tek_srez = s[i : i + 10]
            if tek_srez in hash_table:
                hash_table[tek_srez] += 1
            else:
                hash_table[tek_srez] = 1
            max_repeat = max(max_repeat, hash_table[tek_srez])
        if max_repeat > 1:
            max_keys = [key for key, value in hash_table.items() if value == max_repeat]
            return max_keys
        else:
            return []
