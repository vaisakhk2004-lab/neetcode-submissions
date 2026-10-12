# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        one=l1
        two=l2
        dummy=ListNode()
        current=dummy
        carry=0
        digit=0
        while one or two or carry:
            
            value1 = one.val if one else 0
            value2 = two.val if two else 0
            target = value1 + value2 + carry

            if target>=10:
                carry=target//10
                digit=target%10
                current.next=ListNode(digit)
            else: 
                current.next=ListNode(target)
                carry=0

            one=one.next if one else None
            two=two.next if two else None
            current=current.next
        return dummy.next
        
        