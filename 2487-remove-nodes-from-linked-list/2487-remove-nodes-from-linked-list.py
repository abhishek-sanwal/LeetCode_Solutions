# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        def reverseLL(head):
            
            prev = None
            
            while head:
                
                ref = head.next
                
                head.next = prev
                
                prev = head
                
                head = ref
                
            return prev
        
        head = reverseLL(head)
        
        maxi = -10**18
        
        temp = head
        prev = head
        while temp:
            
            if maxi > temp.val:
                
                prev.next = temp.next
                #print(head)
            else:
                maxi = max(maxi,temp.val)
                prev = temp  
            temp = temp.next
                
        return reverseLL(head)
            
            
            
            
        