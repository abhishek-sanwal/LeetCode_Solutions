# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = head
        while temp:
            nxt = temp.next
            curr = dummy
            
            while curr.next and curr.next.val < temp.val:
                
                curr = curr.next
                
            # Insert temp between curr and curr.next   
            temp.next = curr.next
            curr.next = temp
            temp = nxt
            
        return dummy.next