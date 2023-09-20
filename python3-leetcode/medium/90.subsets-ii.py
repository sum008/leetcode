#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def get_all_subsets(index, cur_res):
            while index < n:
                new_res = cur_res+[nums[index]]
                get_all_subsets(index+1, new_res)
                if tuple(new_res) not in records:
                    result.append(new_res)
                    records.add(tuple(new_res))
                index += 1

        n = len(nums)
        nums = sorted(nums)
        records = set()
        result = [[]]
        get_all_subsets(0, [])
        return result

# @lc code=end
