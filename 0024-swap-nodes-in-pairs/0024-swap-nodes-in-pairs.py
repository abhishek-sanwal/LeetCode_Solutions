# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast =  head
        
        prev = dh = ListNode(next=head)
        
        while fast and fast.next:
            
            ref = fast.next.next
            
            # prev -> 2
            prev.next = fast.next
            
            fast.next.next = fast
            
            fast.next = ref
            
            prev = fast
            
            fast = fast.next
            
        return dh.next
            
            
        
        