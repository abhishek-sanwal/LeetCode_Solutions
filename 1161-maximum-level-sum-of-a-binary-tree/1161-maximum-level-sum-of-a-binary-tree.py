# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        level_map = defaultdict(int)
        maxi = -(sys.maxsize)
        
        def dfs(root,level=1):
            
            if not root:
                
                return 0
            
            level_map[level] += root.val
            
            dfs(root.left,level+1)
            dfs(root.right,level+1)
            
        
        dfs(root)
        
        for i in level_map:
            
            if maxi < level_map[i]:
                
                maxi = level_map[i]
                
                ans = i
        
        return ans
            
            
        
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