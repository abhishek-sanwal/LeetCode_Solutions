# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        maxi = - (10**12)
        
        level = 1
        ans = 0
        que = deque([root])
        
        while que:
            
            curr_level_sum = 0
            
            for _ in range(len(que)):
                
                node = que.popleft()
                curr_level_sum += node.val
                
                if node.left:
                    
                    que.append(node.left)

                if node.right:

                    que.append(node.right)
                    
            if maxi < curr_level_sum:
                
                ans = level
                
                maxi = curr_level_sum
            level += 1
            
        return ans