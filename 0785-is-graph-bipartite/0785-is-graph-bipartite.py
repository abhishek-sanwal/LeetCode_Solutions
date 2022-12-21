class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        adj = graph
        
        n = len(graph)
        
        color = [-1]*(n)

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
                        
                    
        for node in range(n):
            
            if color[node] == -1:
                
                if not bfs(node,adj):
                    
                    return False
            
        return True