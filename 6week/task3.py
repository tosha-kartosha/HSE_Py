"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-k-closest-elements/description/?envType=problem-list-v2&envId=sliding-window
"""


def BinSearch(arr, elem, k):
    if len(arr) == 2:
        if abs(elem - arr[0]) <= abs(elem - arr[1]):
            return 0
        else:
            return 1
    low, high = 0, len(arr) - 1
    mid = (low + high) // 2
    while low < high:
        if arr[mid] == elem:
            return mid
        elif arr[mid] < elem:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if k == 1:
        if mid != 0:

            if abs(elem - arr[mid - 1]) <= abs(elem - arr[mid]):
                ans = mid - 1
            else:
                ans = mid
            if abs(elem - arr[mid + 1]) < abs(elem - arr[mid]):
                ans = mid + 1
            return ans
    if mid + 1 == len(arr):
        return mid
    if abs(elem - arr[mid]) <= abs(elem - arr[mid + 1]):
        return mid
    return mid + 1


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        if x <= arr[0]:
            return arr[0:k]
        if x >= arr[-1]:
            return arr[-k:]
        ind = BinSearch(arr, x, k)
        ans = [arr[ind]]
        left = ind - 1
        right = ind + 1
        while len(ans) != k and left >= 0 and right < len(arr):
            if abs(arr[left] - x) <= abs(arr[right] - x):
                ans = [arr[left]] + ans
                left -= 1
            else:
                ans += [arr[right]]
                right += 1
        while len(ans) < k:
            if left >= 0:
                ans = [arr[left]] + ans
                left -= 1
            else:
                ans += [arr[right]]
                right += 1
        return ans
