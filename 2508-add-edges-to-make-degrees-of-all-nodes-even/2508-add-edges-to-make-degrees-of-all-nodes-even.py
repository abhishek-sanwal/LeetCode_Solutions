class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(set)
        
        for u,v in edges:
            
            adj[u].add(v)
            adj[v].add(u)
        
        odd = 0
        odd_vertices = list()
        for i in range(1,n+1):
        
            if len(adj[i])%2:
            
                odd += 1
                odd_vertices.append(i)
            
        if not odd:
            return True
        
        if odd == 2:
            
            a,b = odd_vertices
            
            for k in range(1,n+1):
                
                if k not in adj[a] and k not in adj[b]:
                    return True
        if odd == 4:
            
            a,b,c,d = odd_vertices
            
            if (a not in adj[b] and c not in adj[d]) or (a not in adj[c] and b not in adj[d]) or (a not in adj[d] and b not in adj[c]):
                
                return True
        return False