#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        def fibs(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n in fib_dict:
                return fib_dict[n]
            else:
                res = fibs(n-1)+fibs(n-2)
                fib_dict[n] = res
                return res
        fib_dict = {}
        return fibs(n)
        
# @lc code=end

