# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []
        temp = prev = head
        while head:
            
            arr.append(head.val)
            head = head.next
        arr.sort()
        i=0
        while prev:
            
            prev.val = arr[i]
            i+=1
            prev = prev.next
            
        return temp