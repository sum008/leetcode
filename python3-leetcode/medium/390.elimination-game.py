#
# @lc app=leetcode id=390 lang=python3
#
# [390] Elimination Game
#

# @lc code=start
class Solution:
    def lastRemaining(self, n: int) -> int:
        def eliminate(n, a, d):
            if n==1:
                return a
            return eliminate(n//2, a+(n//2 -1)*d + d//2, -d*2)
        return eliminate(n,1,2)
        
# @lc code=end

