# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def storeleafs(root,arr):
            
            if root:
                
                if not(root.left or root.right):
                    
                    arr.append(root.val)
                    return 
                
                storeleafs(root.left,arr)
                storeleafs(root.right,arr)
        
        arr1 = list()
        arr2 = list()
        storeleafs(root1,arr1)
        storeleafs(root2,arr2)
        
        return arr1 == arr2
            