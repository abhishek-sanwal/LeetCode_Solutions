# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def addNumbers(l1,l2):
            
            ans = dh = ListNode(-1)

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
                ans.next = node
                ans = ans.next

            while carry:

                node = ListNode(carry % 10)
                ans.next = node
                ans = ans.next
                carry //= 10

            ans.next = None

            return dh.next
        
        def reverseLL(head):
            
            prev = None
            
            while head:
                
                ref = head.next
                head.next = prev
                prev = head
                head = ref
                
            return prev
        
        
        return reverseLL(addNumbers(reverseLL(l1),reverseLL(l2)))
        