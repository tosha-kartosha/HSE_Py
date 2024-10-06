"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/3sum/description/?envType=problem-list-v2&envId=array
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        if nums[0] > 0 or len(nums) <= 2:
            return []
        elif nums[0] == 0:
            if len(nums) >= 3 and nums[1] == nums[2] == 0:
                answer.add(tuple([0, 0, 0]))
            else:
                return []
        else:
            ind = 0
            while ind < len(nums) - 2 and nums[ind] <= 0:
                ost_sum = 0 - nums[ind]
                l_ptr = ind + 1
                r_ptr = len(nums) - 1
                while l_ptr != r_ptr and l_ptr < len(nums):
                    tek_sum = nums[l_ptr] + nums[r_ptr]
                    if tek_sum == ost_sum:
                        tek_arr = tuple(sorted([nums[ind], nums[l_ptr], nums[r_ptr]]))
                        if tek_arr not in answer:
                            answer.add((tek_arr))
                        prev = nums[l_ptr]
                        while nums[l_ptr] == prev and l_ptr != r_ptr:
                            l_ptr += 1
                    elif tek_sum > ost_sum:
                        prev = nums[r_ptr]
                        while nums[r_ptr] == prev and l_ptr != r_ptr:
                            r_ptr -= 1
                    else:
                        prev = nums[l_ptr]
                        while nums[l_ptr] == prev and l_ptr != r_ptr:
                            l_ptr += 1
                ind += 1
        answer = [list(t) for t in answer]
        return answer
