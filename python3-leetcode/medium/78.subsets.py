#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def get_all_subsets(index, cur_res):
            while index < n:
                new_res = cur_res+[nums[index]]
                get_all_subsets(index+1, new_res)
                result.append(new_res)
                index += 1

        n = len(nums)
        result = [[]]
        get_all_subsets(0, [])
        return result


# @lc code=end
