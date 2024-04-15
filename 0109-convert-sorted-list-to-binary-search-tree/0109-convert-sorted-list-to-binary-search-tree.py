# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        temp = head
        
        def middleLL(head):
            
            fast = slow = head
            
            prev = None
            
            while fast and fast.next:
                
                fast = fast.next.next
                prev = slow
                slow = slow.next
            
            prev.next = None
            
            return slow
        
        def recursion(head):
            
            if not head:
                return None
            
            if not head.next:
                
                return TreeNode(head.val)
            
            node = middleLL(head)
            
            # Create node
            nw = TreeNode(node.val)
            
            # for left part
            nw.left = recursion(head)
            
            # For right part
            nw.right = recursion(node.next)
            
            return nw
        
        return recursion(head)
        
        
        