#
# @lc app=leetcode id=1763 lang=python3
#
# [1763] Longest Nice Substring
#

# @lc code=start
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def solve(s):
            if len(s)<=1:
                return ""
            max_substring=""
            for char in s:
                if (char.islower() and char.upper() not in s) or (char.isupper() and char.lower() not in s):
                    k=s.split(char)
                    for ss in k:
                        a1=solve(ss)
                        if len(a1)>len(max_substring):
                            max_substring=a1
                    return max_substring
            return s
        return solve(s)
        
# @lc code=end

