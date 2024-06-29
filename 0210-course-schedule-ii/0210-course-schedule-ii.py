class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       # Kahn's algo for Topo sort
        
        indegree = [0]*numCourses
        
        adj = defaultdict(list)
        
        for v,u in prerequisites:
            
            adj[u].append(v)
            indegree[v] += 1
            
        que = deque()
        # Find nodes with zero degree or zero dependecies or starter nodes
        order = list()
        vis = set()
        
        for node in range(numCourses):
            
            if not indegree[node]:
                
                que.append(node)
                
        while que:
            
            for _ in range(len(que)):
                node = que.popleft()
                order.append(node)
                # Vertices which can be accessed from node
                for adjacent in adj[node]:

                    if adjacent not in vis:
                        indegree[adjacent] -= 1

                        if not indegree[adjacent]:
                            que.append(adjacent)

                        
        return order if len(order) == numCourses else list()
        