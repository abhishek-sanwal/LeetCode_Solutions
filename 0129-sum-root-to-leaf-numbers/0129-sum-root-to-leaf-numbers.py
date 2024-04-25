# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        sumi = 0
        
        def recursion(root,num):
            nonlocal sumi
            if not root:
                return None
            
            # if node is a leaf node
            if not(root.left or root.right):
                
                sumi += (num*10 + root.val)
                return None
            
            recursion(root.left, num * 10 + root.val)
            recursion(root.right, num * 10 + root.val)
            
        recursion(root,0)
        
        return sumi
            