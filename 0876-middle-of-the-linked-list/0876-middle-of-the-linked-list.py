# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            
            return 
        
        slow = fast = head
        
        while fast.next and fast.next.next:
            
            fast = fast.next.next
            
            slow = slow.next
            
        
        slow = slow.next if fast.next else slow
        
        return slow