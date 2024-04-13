# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
#         lists=[[head.val,head]  for head in lists if head]
        
#         heapify(lists)
        
#         dummyhead = curr = ListNode(-1)
        
#         while lists:
            
#             data,node = heappop(lists)
            
#             if node.next:
                
#                 heappush(lists,[node.next.val,node.next])
            
#             curr.next = node
#             curr = curr.next
            
#         return dummyhead.next
        
        
        dummyhead = dh = ListNode(-1)
        
        min_heap = [[head.val,head] for head in lists if head]
        #print(min_heap)
        heapify(min_heap)
        
        while min_heap :
            
            node = heappop(min_heap)[1]
            
            new_node = ListNode(val = node.val)
            dh.next = new_node
            dh = new_node
            
            if node.next:
                heappush(min_heap,[node.next.val,node.next])
                
        #print(min_heap)
        return dummyhead.next
        