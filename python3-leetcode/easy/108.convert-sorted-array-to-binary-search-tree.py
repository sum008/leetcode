#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sortedArrayToBST(self, nums):
            def form_bt(cur_num):
                if len(cur_num)==0:
                    return None
                mid=len(cur_num)//2
                return TreeNode(val=cur_num[mid], left=form_bt(cur_num[0:mid]), right=form_bt(cur_num[mid+1:]))
            return form_bt(nums)
        
# @lc code=end

