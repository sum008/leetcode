#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def find_all_combination(cur_list, res, start):
            if sum(cur_list) > target:
                return
            if sum(cur_list) == target:
                res.append(cur_list.copy())
                return
            while start < len(candidates):
                cur_list.append(candidates[start])
                find_all_combination(cur_list, res, start)
                cur_list.pop()
                start += 1
        res = []
        find_all_combination([], res, 0)
        return res

# @lc code=end
