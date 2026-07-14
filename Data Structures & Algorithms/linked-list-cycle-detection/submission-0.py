# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        temp=head
        address_book=[]
        while(temp!=None):
            if temp in address_book:
                return True
            else:
                address_book.append(temp)
                temp=temp.next
        return False

        