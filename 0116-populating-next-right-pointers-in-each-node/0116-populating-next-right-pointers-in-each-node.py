"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            
            return 
        
        que = deque([root])
        
        while que:
            
            prev = None
            
            for _ in range(len(que)):
                
                node = que.popleft()

                if node.left:

                    que.append(node.left)
                    
                if node.right:
                    
                    que.append(node.right)
                    
                if prev:
                    
                    prev.next = node
                    
                prev = node
                
        return root