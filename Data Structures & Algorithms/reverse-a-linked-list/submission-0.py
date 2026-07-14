# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return head
        if(head.next==None):
            return head
        
        pre=None
        current=head
        next=head.next
        while(next!=None):
            
            current.next=pre
            pre=current
            current=next
            next=current.next
        
        current.next=pre
            
        return current

        