#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def check(head, n):
            if head == None:
                return True
            val = head.val
            stk.append(val)
            last = check(head.next, n+1)
            if last and stk[len(stk)-n] == val:
                return True
            return False
        stk = []
        return check(head, 1)

# @lc code=end
