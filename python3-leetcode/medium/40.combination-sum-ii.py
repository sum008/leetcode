#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def find_all_combination(cur_list, res, start):
            if sum(cur_list) > target:
                return
            if sum(cur_list) == target:
                x = cur_list.copy()
                xx = ''.join(x)
                if xx not in d:
                    res.append(x)
                    d.add(xx)
                # print(res)
                return
            while start < len(candidates):
                cur_list.append(candidates[start])
                find_all_combination(cur_list, res, start+1)
                cur_list.pop()
                start += 1
        res = []
        d = set()
        candidates = sorted(candidates)
        if sum(candidates) >= target:
            find_all_combination([], res, 0)
        return res

# @lc code=end
