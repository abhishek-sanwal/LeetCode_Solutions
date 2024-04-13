# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyhead = dh = ListNode(val= -1,next=head)
        
        last = first = head
        
        for _ in range(n-1):
            
            first = first.next
            
        while first.next:
            
            dh = last
            last = last.next
            
            first = first.next
            
        dh.next = last.next
        
        return dummyhead.next