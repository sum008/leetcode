#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def find_winner(index, stk):
            if len(stk) == 1:
                return stk[0]
            stk = stk[index+1:] + stk[0:index]
            return find_winner((k-1) % len(stk), stk)
        stk = list(range(1, n+1))
        return find_winner((k-1) % n, stk)

# @lc code=end
