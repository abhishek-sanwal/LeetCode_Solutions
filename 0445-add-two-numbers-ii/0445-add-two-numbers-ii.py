# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def ReverseaddNumbers(l1,l2):
            
            ans = dh = ListNode(-1)
            prev = None
            sumi = carry = 0

            while l1 or l2:

                val1 = val2 = 0

                if l1:
                    val1 = l1.val
                    l1 = l1.next

                if l2:
                    val2 = l2.val
                    l2 = l2.next
                carry, sumi = divmod( val1 + val2 + carry,10)
                #print(carry,sumi)
                node = ListNode(sumi)
                node.next = prev
                prev = node

            while carry:

                node = ListNode(carry % 10)
                node.next = prev
                prev = node
                carry //= 10

            return prev
        
        def reverseLL(head):
            
            prev = None
            
            while head:
                
                ref = head.next
                head.next = prev
                prev = head
                head = ref
                
            return prev
        
    
        return ReverseaddNumbers(reverseLL(l1),reverseLL(l2))
        