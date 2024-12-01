"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        cur_ptr = 0
        len_arr = len(arr)
        if cur_ptr + k <= len_arr:
            cur_sum = sum(arr[:k])
            if (cur_sum / k) >= threshold:
                count += 1
            cur_ptr += 1
            while cur_ptr + k <= len_arr:
                cur_sum = cur_sum - arr[cur_ptr - 1] + arr[cur_ptr + k - 1]
                if (cur_sum / k) >= threshold:
                    count += 1
                cur_ptr += 1
        return count
