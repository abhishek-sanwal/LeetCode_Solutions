# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        idx = 0
        stack = list()
        ans = []
        
        while head:
            val = head.val
            while stack and stack[-1][0] < val:
                
                ans[stack.pop()[1]] = val
                
            stack.append([val,idx])
            head = head.next
            ans.append(0)
            idx += 1
            
        return ans 
    
        for idx,val in enumerate(arr):
            
            while stack and arr[stack[-1]] < val:
                
                ans[stack.pop()] = val
                
            stack.append(idx)
            
        return ans