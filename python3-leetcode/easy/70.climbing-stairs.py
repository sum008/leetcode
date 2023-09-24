#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        def calc_steps(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in d:
                return d[n]
            k = calc_steps(n-1) + calc_steps(n-2)
            d[n] = k
            return k
        d = {}
        return calc_steps(n)

# @lc code=end
