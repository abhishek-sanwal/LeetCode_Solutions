# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        first_kth = last_kth = head
        
        for _ in range(k-1):
            
            first_kth = first_kth.next
            
        temp = first_kth
        
        while temp.next:

            temp = temp.next
            last_kth =last_kth.next
        #print(last_kth.val) 
        last_kth.val, first_kth.val = first_kth.val , last_kth.val
        
        return head