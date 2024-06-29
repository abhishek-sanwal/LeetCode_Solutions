class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Kahn's algo for Topo sort
        
        indegree = [0]*numCourses
        
        adj = defaultdict(list)
        
        for u,v in prerequisites:
            
            adj[u].append(v)
            indegree[v] += 1
            
        que = deque()
        # Find nodes with zero degree or zero dependecies or starter nodes
        order = list()
        for node in range(numCourses):
            
            if not indegree[node]:
                
                que.append(node)
                order.append(node)
                
        while que:
            
            for _ in range(len(que)):
                
                node = que.popleft()
                
                # Vertices which can be accessed from node
                for adjacent in adj[node]:
                    
                    indegree[adjacent] -= 1
                    
                    if not indegree[adjacent]:
                        que.append(adjacent)
                        order.append(adjacent)
                        
        return reversed(order) if len(order) == numCourses else list()
        
        adj = defaultdict(list)
        
        for u,v in prerequisites:
            
            adj[u].append(v)
            
        
        stack = list()
        vis = set()
        def dfs(node):
            
            vis.add(node)
            
            for adjacent in adj[node]:
                
                if adjacent not in vis:
                    dfs(adjacent)
        
            stack.append(node)
            
        for node in range(numCourses):
            
            if node not in vis:
                
                dfs(node)
        return stack
        stack = list()
        
        def dfs(node):

            vis.add(node)
            
            for adja in adj[node]:
                
                if adja not in vis:
                    dfs(adja)
                    
            stack.append(node)
            
            return None
        
        vis = set()
        
        for node in range(numCourses):
            dfs(node)
        print(stack)
        return stack[::-1]