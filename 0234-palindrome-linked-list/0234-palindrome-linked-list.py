# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def findMiddle(head):
            
            slow = fast = head
            
            while fast and fast.next:
                
                fast = fast.next.next
                slow = slow.next
                
            return slow
                
        def reverseLL(head):
            
            temp = None
            
            while head:
                
                x = head.next
                
                head.next = temp
                temp = head
                head = x
            
            return temp
        
        new_head = reverseLL(findMiddle(head))
        
        while head and new_head:
            
            if head.val != new_head.val:
                
                return False
            
            head = head.next
            new_head = new_head.next
            
        return True
        
        
#         0(n)  finding middle node
#         0(n) checking palindrome
        
#         1 2 3 4 5
        
#         a1 == a5
#         a2 == a4
#         a3 == a3
        
        
        
#         1 2 3 4 5
        
#         1 2 3 4
        
#         1 2 3 5 4
        
#         1 2 3 4
        
        # Two pass Solution
        arr = []
        temp = head
        while temp:
            
            arr.append(temp.val)
            
            temp = temp.next
            
        return arr == arr[::-1]