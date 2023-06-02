
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        
        def distance(x1,y1,x2,y2,radius):
            
            x = ((x1-x2)**2 + (y1-y2)**2)**0.5
            
            return x <= radius
        
        adj = defaultdict(list)
        
        
        for i in range(len(bombs)):
            
            for j in range(len(bombs)):
                
                if distance(bombs[i][0],bombs[i][1],bombs[j][0],bombs[j][1],bombs[i][2]):
                    
                    adj[i].append(j)
        
        
        maxi = 0
        #print(adj)
        def dfs(source,vis):
            
            vis.add(source)
            
            for adja in adj[source]:
                
                if adja not in vis:
                
                    dfs(adja,vis)
            #print(vis,source)
            return len(vis)
                    
        for i in range(len(bombs)):
            
            maxi = max(maxi,dfs(i,set()))
                
        
        return maxi
                