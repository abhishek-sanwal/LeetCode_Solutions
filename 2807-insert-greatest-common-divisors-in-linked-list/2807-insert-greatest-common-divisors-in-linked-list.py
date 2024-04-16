# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        
        while temp and temp.next:
            
            node = ListNode(gcd(temp.val,temp.next.val))
            x = temp.next
            temp.next = node
            node.next = x
            temp = x
            
        return head
            