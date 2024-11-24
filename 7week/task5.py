"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-turbulent-subarray/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        left_ptr = 0
        right_ptr = 1
        check = True
        while right_ptr < len(arr) and arr[left_ptr] == arr[right_ptr]:
            left_ptr = right_ptr
            right_ptr += 1
        if right_ptr == len(arr):
            return 1
        else:
            check = True if arr[left_ptr] < arr[right_ptr] else False
            tek_rez = 2
            max_rez = 2
        right_ptr += 1
        while right_ptr < len(arr):
            check_tek = True if arr[right_ptr - 1] < arr[right_ptr] else False
            if check_tek != check and arr[right_ptr - 1] != arr[right_ptr]:
                check = check_tek
                tek_rez += 1
                max_rez = max(max_rez, tek_rez)
            else:
                if arr[right_ptr - 1] == arr[right_ptr]:
                    tek_rez = 1
                else:
                    tek_rez = 2
            right_ptr += 1
            max_rez = max(max_rez, tek_rez)
        return max_rez
