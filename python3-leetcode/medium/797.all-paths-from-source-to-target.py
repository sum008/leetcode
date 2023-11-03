#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        l = len(graph)
        start=graph[0]
        d = {}
        final_res=[]
        for i in range(1,l):
            d[i]=graph[i]
        def solve(lis, res):
            for i in lis:
                if i==l-1:
                    final_res.append(res+[i])
                    continue
                solve(d[i], res+[i])
        solve(start, [0])
        return final_res
        
# @lc code=end

