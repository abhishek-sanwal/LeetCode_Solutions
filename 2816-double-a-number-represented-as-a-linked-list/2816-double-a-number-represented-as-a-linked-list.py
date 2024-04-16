# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            
            return None
        
        temp = head
        
        if head.val > 4:
            
            node = ListNode(1)
            node.next = head
            head = node
            
        while temp:
            
            temp.val = (temp.val * 2) % 10
            
            if temp.next and temp.next.val > 4:
                
                temp.val += 1
                
            temp = temp.next
            
        return head 