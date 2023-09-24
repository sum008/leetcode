#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        def calc_steps(cur_sum, n):
            if cur_sum == n:
                return 1
            if cur_sum > n:
                return 0
            return calc_steps(cur_sum+steps[0], n) + calc_steps(cur_sum+steps[1], n)
        steps = [1, 2]
        return calc_steps(0, n)

# @lc code=end
