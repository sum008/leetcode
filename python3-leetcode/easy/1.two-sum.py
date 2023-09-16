#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        res = []
        for index, ele in enumerate(nums):
            num_dict[ele] = index

        for index, ele in enumerate(nums):
            if target-ele in num_dict and index != num_dict[target-ele]:
                res.append(index)
                res.append(num_dict[target-ele])
                break

        return res

# @lc code=end
