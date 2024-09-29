"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/integer-to-roman/description/?envType=problem-list-v2&envId=string
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        delete_value = 0

        while num != 0:
            if str(num)[0] not in "49":
                tek_alf = {
                    "1": "I",
                    "5": "V",
                    "10": "X",
                    "50": "L",
                    "100": "C",
                    "500": "D",
                    "1000": "M",
                }
            else:
                tek_alf = {
                    "4": "IV",
                    "9": "IX",
                    "40": "XL",
                    "90": "XC",
                    "400": "CD",
                    "900": "CM",
                }
            for key in tek_alf:
                if int(key) > num:
                    break
                tek_num = tek_alf[key]
                delete_value = int(key)
            res += tek_num
            num -= delete_value
        return res
