class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        '''
               1(a)
            
            (b)2     3 (b)
            
            
            4(a)
            
                    1 (a)
                
                (b)2      3(b)
            
        '''
        
        # check if graph is bipartile or not
        # check graph is 2 colourable or not
        
        
        adj = defaultdict(list)
        
        for u,v in dislikes:

            adj[u].append(v)
            adj[v].append(u)
    
        color = [-1]*(n+1)

        def bfs(source,adj):
                
            nonlocal color
            
            que = deque([source])

            color[source] = 0
            
            while que:

                node = que.popleft()
                parent_color = color[node]
        
                for adjacent in adj[node]:

                    if color[adjacent]==-1:
                        color[adjacent] = 1-color[node]
                        
                        que.append(adjacent)
                        
                    if color[adjacent] == color[node]:
                        
                        return False
            
            return True
                        
                    
        for node in range(1,n+1):
            
            if color[node] == -1:
                
                if not bfs(node,adj):
                    
                    return False
            
        return True