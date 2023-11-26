#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            r.append(root.val)
            inorder(root.right)
        def form_bbst(r):
            if len(r)==0:
                return None
            mid=len(r)//2
            return TreeNode(val=r[mid], left=form_bbst(r[0:mid]), right=form_bbst(r[mid+1:]))
        r=[]
        inorder(root)
        return form_bbst(r)
        
# @lc code=end

