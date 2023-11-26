#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def solve(n, r, c):
            all_same=True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        all_same=False
                        break
                if not all_same:
                    break
            if all_same:
                return Node(grid[r][c], True)
            n=n//2
            topleft=solve(n, r, c)
            topright=solve(n, r, n+c)
            bottomleft=solve(n, r+n, c)
            bottomright=solve(n, r+n, c+n)
            return Node(grid[r][c], False, topleft, topright, bottomleft, bottomright)
        return solve(len(grid), 0, 0)
        
# @lc code=end

