# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second=slow.next
        slow.next=None
        pre = None
        while second:
            temp=second.next
            second.next=pre
            pre=second
            second=temp
        second=pre
        first=head
        while second:
            temp1=first.next
            sec=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=sec
            
        

            
            



        

        