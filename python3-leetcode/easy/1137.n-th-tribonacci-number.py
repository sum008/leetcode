#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        def calc_tribonacci(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            if n in d:
                return d[n]
            x = calc_tribonacci(n-1)+calc_tribonacci(n-2)+calc_tribonacci(n-3)
            d[n] = x
            return x
        d = {}
        return calc_tribonacci(n)

# @lc code=end
