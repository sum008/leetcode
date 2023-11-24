#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(nums):
            if len(nums)==0:
                return None
            m=max(nums)
            i=nums.index(m)
            return TreeNode(nums[i], solve(nums[0:i]), solve(nums[i+1:]))
        return solve(nums)
        
# @lc code=end

