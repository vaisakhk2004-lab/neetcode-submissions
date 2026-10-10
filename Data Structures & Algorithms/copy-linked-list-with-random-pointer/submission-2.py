"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies={}
        current=head
        while  current:
            val=current.val
            copies[current]=Node(x=val)
            current=current.next
        current=head
        while current:
            copy=copies[current]
            copy.next=copies.get(current.next)
            copy.random=copies.get(current.random)
            current=current.next
        return copies[head] if head else None


            


        