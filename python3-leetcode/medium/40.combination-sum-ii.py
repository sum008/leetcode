#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def find_all_combination(cur_list, res, start, cur_str, cur_sum):
            if cur_sum == target:
                if cur_str not in d:
                    res.append(cur_list.copy())
                    d.add(cur_str)
                return
            if sum(candidates[start:])+cur_sum < target or \
                    (start < len(candidates) and candidates[start] > target):
                return
            while start < len(candidates):
                if cur_sum+candidates[start] > target:
                    return
                # if cur_sum+candidates[start] <= target:
                final_str = cur_str+str(candidates[start])
                final_sum = cur_sum + candidates[start]
                cur_list.append(candidates[start])
                find_all_combination(
                    cur_list, res, start+1, final_str, final_sum)
                cur_list.pop()
                start += 1
                if final_sum == target:
                    return
        res = []
        d = set()
        candidates = sorted(candidates)
        find_all_combination([], res, 0, "", 0)
        return res

# @lc code=end
