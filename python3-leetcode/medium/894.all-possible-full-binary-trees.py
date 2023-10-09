#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def get_all_fbt(count):
            if count in cache:
                return cache[count]
            res = []
            for c in range(0, count):
                l = count-1-c
                r = c
                left, right = get_all_fbt(l), get_all_fbt(r)
                for a in left:
                    for b in right:
                        res.append(TreeNode(val=0, left=a, right=b))
            cache[count] = res
            return res

        cache = {0:[],1:[TreeNode()]}
        a = get_all_fbt(n)
        # res_list.append(head)
        print(len(a))
        return a

# @lc code=end
