# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #print(head)
        if not(head and k):
            
            return head
        
        temp = head
        length = 0
        # Calculate length of linked list
        while temp:

            temp = temp.next
            length += 1
            
        k %= length 
        
        if k==0:
            return head
        
        # Now find kth element from the last and its prev_element
        
        prev = kth = head
        
        temp = head
        
        for _ in range(k-1):
            
            temp = temp.next
            
        
        while temp.next:
            
            temp = temp.next
            prev = kth
            kth = kth.next
            
        prev.next = None
        
        new_head = kth
        
        # join the last element of linked list to the head
        while kth.next:
            
            kth = kth.next
        
        kth.next = head
        
        return new_head
        