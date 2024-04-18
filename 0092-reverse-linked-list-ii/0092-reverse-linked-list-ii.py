# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyHead = dh = ListNode(-1,head)
        l = r = head
        prev = dh
        idx = 1
        
        # Find left reverse point and its previous element
        while head and idx < left:
            idx += 1
            prev = head
            head = head.next
        #print(head.val,prev.val)
        if not head:
            return dummyHead.next
        
        # prev = 1
        l = head
        # l = 2
        # prev.next = l
        
        # Find right reverse point and its next element
        while head and idx < right:
            idx += 1
            head = head.next
        
        if not head:
            return dummyHead.next
        
        r = head # 4
        nxt = r.next # 5
        
        # Now reverse linkedlist between left and right
        
        new_head = None
        new_tail = l
        while l != nxt:
            
            x = l.next
            l.next = new_head
            new_head = l
            l = x
        
        #print(prev.val, new_head.val, new_tail.val, nxt.val)
        # Link connections
        prev.next = new_head
        new_tail.next = nxt
        
        return dummyHead.next