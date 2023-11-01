#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def solve(index, subset):
            if index>=len(nums):
                return subset
            res=subset
            while index<len(nums):
                res+=solve(index+1, subset^nums[index])
                index+=1
            return res
        return solve(0,0)
        
# @lc code=end

