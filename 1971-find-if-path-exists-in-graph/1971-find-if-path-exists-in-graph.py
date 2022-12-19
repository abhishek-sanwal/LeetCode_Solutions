class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        def bfs(source,destinationa,adj):
            
            que = deque([source])
            
            while que:
                
                node = que.popleft()
                vis[node] = True
                #print(node,vis)
                for adjacent in adj[node]:
                    
                    if adjacent == destination:
                        
                        return True
                    
                    if not vis[adjacent]:
                        
                        que.append(adjacent)
                        
            return False
        
        
        adj = defaultdict(list)
        m = -1
        for edge in edges:
            
            m = max(m,edge[0],edge[1])
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        vis = [False] * (m+1)
        
        return source == destination or bfs(source,destination,adj)
            