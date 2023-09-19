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
                cur_res = ''.join([str(i) for i in fixed])
                result.append(fixed.copy())
                record_keep.add(cur_res)
                return
            start = 0
            while start < len(remaining):
                fixed.append(remaining[start])
                temp = remaining[0:start]+remaining[start+1:]
                f1 = ''.join([str(i) for i in fixed])
                f2 = ''.join([str(i) for i in temp])
                if f1+f2 in record_keep:
                    start += 1
                    fixed.pop()
                    continue
                get_all_permutations(fixed, temp)
                fixed.pop()
                start += 1

        result = []
        record_keep = set()
        get_all_permutations([], nums)
        return result

# @lc code=end
