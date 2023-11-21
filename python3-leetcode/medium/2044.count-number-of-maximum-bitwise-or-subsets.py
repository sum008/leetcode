#
# @lc app=leetcode id=2044 lang=python3
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#

# @lc code=start
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def solve(index, count, cur_or, max_or):
            for i in range(index, len(nums)):
                if cur_or | nums[i] > max_or:
                    max_or = cur_or | nums[i]
                    count=1
                elif cur_or | nums[i] == max_or:
                    count+=1
                max_or, count=solve(i+1, count, cur_or|nums[i], max_or)
            return max_or, count
        return solve(0, 0, 0,0)[1]
        
# @lc code=end

