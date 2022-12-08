# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def solve2(self,root, low, high):
        
        curr_sum=0
        
        if root is None:
            return 0
        
        if root.val >= low and root.val <= high:
            #print(self.curr_sum)
            #print(curr_sum)
            curr_sum = root.val
            print(curr_sum) 

        if root.val > low  or root.val > high:

            return curr_sum + self.solve2(root.left,low,high)
        return curr_sum + self.solve2(root.right,low,high)
        
        
            
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if not root :
            
            return 0
        
        if low <=  root.val <= high:
            #print(root.val)
            return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        
        return self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        
        
        
        