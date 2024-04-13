# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
#         when slow is at head, fast points at the first node for swapping
# when fast is at the end, slow points at the second node for swapping
        
        dh = prev_kth = prev_last = ListNode(-1,next=head)
        first_kth = last_kth = head
        
        for _ in range(k-1):
            
            prev_kth = first_kth
            first_kth = first_kth.next
            
        temp = first_kth
        
        while temp.next:

            temp = temp.next
            prev_last = last_kth
            last_kth =last_kth.next
        
        if first_kth == last_kth:
            
            return head
        
        prev_kth.next = last_kth
        prev_last.next = first_kth
        
        last_kth.next , first_kth.next = first_kth.next, last_kth.next
        
        return dh.next