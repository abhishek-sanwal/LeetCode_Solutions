class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's algo for Topo sort
        
        indegree = [0]*numCourses
        
        adj = defaultdict(list)
        
        for v,u in prerequisites:
            
            adj[u].append(v)
            indegree[v] += 1
        
        que = deque()
        # Find nodes with zero degree or zero dependecies or starter nodes
        order = list()
        for node in range(numCourses):
            
            if not indegree[node]:
                
                que.append(node)
                
        while que:
            
            for _ in range(len(que)):
                
                node = que.popleft()
                order.append(node)
                # Vertices which can be accessed from node
                for adjacent in adj[node]:
                    
                    indegree[adjacent] -= 1
                    
                    if not indegree[adjacent]:
                        que.append(adjacent)
                
        return len(order) == numCourses