#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def solve(index, subset):
            res=0
            while index<len(nums):
                res+=solve(index+1, subset+[nums[index]])
                cur_subset=subset+[nums[index]]
                x=0
                for i in range(0,len(cur_subset)):
                    x = x ^ cur_subset[i]
                res+=x
                index+=1
            return res
        return solve(0,[])
        
# @lc code=end

