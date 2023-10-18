#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add_nums(l1, l2, carry, temp):
            if l1 == None and l2 == None:
                if carry == 1:
                    temp.next = ListNode(val=carry)
                    temp = temp.next
                return
            a = 0 if l1 == None else l1.val
            b = 0 if l2 == None else l2.val
            cur_val = carry+a+b
            if cur_val > 9:
                carry = 1
                cur_val = cur_val - 10
            else:
                carry = 0
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            temp.next = ListNode(val=cur_val)
            temp = temp.next
            add_nums(l1, l2, carry, temp)

        head = ListNode()
        temp = head
        add_nums(l1, l2, 0, temp)
        return head.next

# @lc code=end
