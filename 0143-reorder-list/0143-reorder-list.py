# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # find the middle element of linkedlist
        
        if not (head and head.next):
            return head
        
        temp = middle = head
        prev_middle = None
        while temp and temp.next:
            
            temp = temp.next.next
            prev_middle = middle
            middle = middle.next
            
        
        # We need to reverse Linked List from middle
        
        prev = None
        
        while middle:
            ref = middle.next
            middle.next = prev
            prev = middle
            middle = ref
    
        prev_middle.next = None
        
        head1, head2 = head, prev
        
        while head1:
            
            nextt = head1.next
            head1.next = head2
            x = head2.next
            head2.next = nextt
            if not nextt:
                head1.next.next = x
            head1 = nextt
            head2 = x
            
        return head
        
        curr_list = head
        
        while temp != prev:
            
            curr_list.next = prev
            curr_list = curr_list.next
            
            temp.next.next
            
            
        return head
            
            
        