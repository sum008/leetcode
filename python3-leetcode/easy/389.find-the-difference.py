#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        s = sorted(s)
        t = sorted(t)
        # d_s = {}
        # d_t = {}
        # for i in s:
        #     if i in d_s:
        #         d_s[i] = d_s[i]+1
        #     else:
        #         d_s[i] = 1
        # for i in t:
        #     if i in d_t:
        #         d_t[i] = d_t[i]+1
        #     else:
        #         d_t[i] = 1
        # for i in d_t.keys():
        #     if i in d_s and d_t[i]>d_s[i]:
        #         return i
        #     elif i not in d_s:
        #         return i
        for index, i in enumerate(s):
            if t[index] != i:
                return t[index]
        return t[index+1]

# @lc code=end
