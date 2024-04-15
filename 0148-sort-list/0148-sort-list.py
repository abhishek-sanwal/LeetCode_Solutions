# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Merge sort  on Linked List
        
        def merge(head1,head2):
            
            dh = dummyHead = ListNode(-1)
            
            while head1 or head2:
                
                if head1 and head2:
                    
                    if head1.val < head2.val:
                        node = ListNode(head1.val)
                        dh.next = node
                        dh = node
                        head1 = head1.next
                        
                    else:
                        node = ListNode(head2.val)
                        dh.next = node
                        dh = node
                        head2 = head2.next
                    
                elif head1:
                    
                    node = ListNode(head1.val)
                    dh.next = node
                    dh = node
                    head1 = head1.next
                    
                elif head2:
                    node = ListNode(head2.val)
                    dh.next = node
                    dh = node
                    head2 = head2.next
                
            return dummyHead.next
        
        def merge_sort(head):
            
            if not head or not head.next:
                
                return head
            
            # Find middle element of linked list and cut it in two parts
            
            slow = fast = head
            prev = None
            
            while fast and fast.next:
                
                fast = fast.next.next
                prev = slow
                slow = slow.next
            
            prev.next = None
            
            left = merge_sort(head)
            right = merge_sort(slow)
            
            return merge(left,right)
        return merge_sort(head)
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