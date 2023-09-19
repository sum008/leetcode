#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
import math


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def get_all_permutations(fixed, remaining, cur_res):
            if len(remaining) == 0:
                result.append(fixed.copy())
                return
            start = 0
            while start < len(remaining):
                fixed.append(remaining[start])
                get_all_permutations(fixed,
                                     remaining[0:start]+remaining[start+1:], cur_res)
                fixed.pop()
                start += 1

        n = len(nums)
        result = []
        get_all_permutations([], nums, [])
        return result


# @lc code=end
