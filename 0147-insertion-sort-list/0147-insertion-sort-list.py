# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-float('inf'))
        while head:
            nxt = head.next
            cur = dummy
            while cur.next and cur.next.val < head.val: cur = cur.next
            head.next = cur.next
            cur.next = head
            head = nxt
        return dummy.next
        
        if not(head and head.next):
            
            return head
        
        dummyHead = dh = ListNode(-1,head)
        curr =  head.next
        # dh ->[4,2,1,3]
            #temp =4  prev =dh curr = 2
            #x = 1
        while curr:
            temp = head
            prev = dh
            while temp.val < curr.val:
                prev = temp
                temp = temp.next
            
            # Insert after prev and before temp
            prev.next = curr
            x = curr.next
            
            if curr != temp:
                curr.next = temp
                
            curr = x
            print(dh.next)
        return dummyHead.next