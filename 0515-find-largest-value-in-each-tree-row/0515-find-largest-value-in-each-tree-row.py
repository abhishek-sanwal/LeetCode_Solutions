# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            
            return []
        
        que = deque([root])
        
        max_list = []
        
        while que:
            
            max_list.append(-sys.maxsize)
            
            for _ in range(len(que)):
                
                node = que.popleft()
                
                max_list[-1] = max(max_list[-1], node.val)
                
                node.left is not None and que.append(node.left)
                
                node.right is not None and que.append(node.right)
                
        return max_list
                    
                
                
                
                