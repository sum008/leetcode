#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def solve(node, cur_str):
            x = cur_str
            if node.left != None:
                x = cur_str+"->"+str(node.left.val)
                solve(node.left, x)
            if node.right != None:
                x = cur_str+"->"+str(node.right.val)
                solve(node.right, x)
            if node.right == None and node.left == None:
                res.append(x)
        res = []
        solve(root, str(root.val))
        return res

# @lc code=end
