# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = list1
        temp2 = list2
        
        dummyHead = dh = ListNode(-1)
        
        while temp1 or temp2:
            
            if temp1 and temp2:
            
                if min(temp1.val,temp2.val) == temp1.val:

                    dummyHead.next = temp1

                    temp1 = temp1.next

                else:

                    dummyHead.next = temp2

                    temp2 = temp2.next
            
            elif temp1:
                
                
                dummyHead.next = temp1
                
                temp1 = temp1.next
                
            else:
                
                dummyHead.next = temp2
                
                temp2 = temp2.next
                
            dummyHead = dummyHead.next

        return dh.next
            
        