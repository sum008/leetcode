#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def get_all_permutations(fixed, remaining):
            if len(remaining) == 0:
                result.append(fixed)
                record_keep.add(tuple(fixed))
                return
            for start in range(0, len(remaining)):
                if tuple(fixed+[remaining[start]] + remaining[0:start]+remaining[start+1:]) in record_keep:
                    continue
                get_all_permutations(
                    fixed+[remaining[start]], remaining[0:start]+remaining[start+1:])

        result = []
        record_keep = set()
        get_all_permutations([], nums)
        return result

# @lc code=end
