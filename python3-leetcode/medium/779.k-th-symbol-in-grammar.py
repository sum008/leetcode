#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def kth_symbol(k):
            if k == 1:
                return 0
            if k % 2 != 0:
                return kth_symbol((k+1)//2)
            else:
                return 1 if kth_symbol(k//2) == 0 else 0
        return kth_symbol(k)

# @lc code=end
