#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def form_binary(self, node, cur_binary, res):
        final_binary = cur_binary + str(node.val)
        if node.left != None:
            res = self.form_binary(node.left, final_binary, res)
        if node.right != None:
            res = self.form_binary(node.right, final_binary, res)

        if node.left == None and node.right == None:
            return res + int(final_binary, 2)
        return res

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        node = root
        return self.form_binary(node, "", 0)


# @lc code=end
