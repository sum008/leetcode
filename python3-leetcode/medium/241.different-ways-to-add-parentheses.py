#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def solve(cur_exp):
            if cur_exp.isdigit():
                dp[cur_exp]=[int(cur_exp)]
                return [int(cur_exp)]
            if cur_exp in dp:
                return dp[cur_exp]
            res=[]
            for i in range(0,len(cur_exp)):
                if cur_exp[i] in ("-","+","*"):
                    res1=solve(cur_exp[0:i])
                    res2=solve(cur_exp[i+1:])
                    for a in res1:
                        for b in res2:
                            if cur_exp[i]=="+":
                                res.append(a+b)
                            elif cur_exp[i]=="-":
                                res.append(a-b)
                            else:
                                res.append(a*b)
            dp[cur_exp]=res
            return res
        dp={}
        return solve(expression)
        
# @lc code=end

