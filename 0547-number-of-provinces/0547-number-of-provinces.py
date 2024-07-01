class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        adj = defaultdict(list)
        
        for i in range(len(isConnected)):
            
            for j in range(len(isConnected[i])):
                
                if isConnected[i][j] == 1 and i!=j:
                    
                    # Means edge from i to j
                    
                    adj[i].append(j)
                    
        vis = set()
        
        def dfs(node):
            
            vis.add(node)
            
            for adjacent in adj[node]:
                
                if adjacent not in vis:
                    
                    dfs(adjacent)
                    
            return None
            
        count = 0
        for i in range(len(isConnected)):
            
            if i not in vis:
                
                dfs(i)
                count += 1
                
        return count