# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            
            return []
        
        que = deque([root])
        
        ans = []
        
        while que:
            for _ in range(len(que)):
                
                node = que.popleft()
                
                if node.left:
                    
                    que.append(node.left)
                    
                if node.right:
                    
                    que.append(node.right)
            ans.append(node.val)
        return ans