# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:

            return

        
        oddtail = oddhead = ListNode(-1)
        eventail = evenhead = ListNode(-1)
        
        while head and head.next:
            
            oddtail.next = head
            eventail.next = head.next

            oddtail = oddtail.next
            eventail = eventail.next

            head = head.next.next
        #print(head)
        if head:
            oddtail.next = head
            oddtail = oddtail.next
        #print(oddtail.val,eventail.val)
        oddtail.next = evenhead.next
        eventail.next = None

        return oddhead.next