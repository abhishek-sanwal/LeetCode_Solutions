# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        #[we can loot parent and its child]
        hashmap =  {}
        
        def recursion(root):
            
            if not root:
                
                return 0
            
            
            x = 0
            
            if root.left and root.left.left:
                
                if id(root.left.left) not in hashmap:
                    
                    hashmap[id(root.left.left)] = recursion(root.left.left)
                
                x = hashmap[id(root.left.left)]
                
            y  = 0
            
            if root.left and root.left.right:
                
                if id(root.left.right) not in hashmap:
                    
                    hashmap[id(root.left.right)] = recursion(root.left.right)
                
                y = hashmap[id(root.left.right)]
                
            w = 0
            if root.right and root.right.right:
                
                if id(root.right.right) not in hashmap:
                    
                    hashmap[id(root.right.right)] = recursion(root.right.right)
                
                w = hashmap[id(root.right.right)]
                
            z  = 0
            
            if root.right and root.right.left:
                
                if id(root.right.left) not in hashmap:
                    
                    hashmap[id(root.right.left)] = recursion(root.right.left)
                
                z = hashmap[id(root.right.left)]
                
            
            return max(recursion(root.left) + recursion(root.right),x+y+z+w+root.val)
            
            
        return recursion(root)
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        k = 0
        def houseRobber1(arr):
            
            nums = arr
        
            prev = curr  = 0

            for i in range(len(nums)):

                prev,curr = curr,max(curr,nums[i] + prev)

            return curr
        
        que = deque([root])
        arr = list()
        while que:
            curr = 0
            for _ in range(len(que)):
                
                node = que.popleft()
                curr += node.val
                if node.left:
                    
                    que.append(node.left)
                
                if node.right:
                    
                    que.append(node.right)
            
            arr.append(curr)
                
        return houseRobber1(arr)