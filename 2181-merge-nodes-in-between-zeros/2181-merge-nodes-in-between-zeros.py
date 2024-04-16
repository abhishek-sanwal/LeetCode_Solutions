# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = dh = ListNode(-1)
        
        while head.next:
            curr_sumi = 0
            head = head.next
            while head and head.val != 0:
                curr_sumi += head.val
                head = head.next
            node = ListNode(curr_sumi)
            dh.next = node
            dh = node
            
        return dummyHead.next