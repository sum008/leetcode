#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp=head
        l=[]
        count=0
        while temp:
            l.append(temp)
            temp=temp.next
            count+=1
        f_end=l[0:(count//2)+1]
        l_end=l[(count//2)+1:]
        for i in f_end:
            i.next=None
        for i in l_end:
            i.next=None
        count=0
        while len(l_end)>0:
            f_end.insert(count+1, l_end.pop())
            if count>0:
                count+=2
            elif count==0:
                count=2
        temp=head
        for i in range(1, len(f_end)):
            temp.next=f_end[i]
            temp=temp.next
        
# @lc code=end

