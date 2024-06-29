class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        anchestors = [set() for _ in range(n)]
        
        adj = defaultdict(list)
        for u,v in edges:
            
            adj[u].append(v)
        
        stack = list()
        vis = set()
        def dfs(node):
            
            vis.add(node)
            
            for adjacent in adj[node]:
                
                if adjacent not in vis:
                    dfs(adjacent)
        
            stack.append(node)
            
        for node in range(n):
            
            if node not in vis:
                
                dfs(node)
        
        while stack:
            node = stack.pop()
            for vertice in adj[node]:
                anchestors[vertice].add(node)
                anchestors[vertice].update(anchestors[node])
        # del stack     

        for index in range(len(anchestors)):
            anchestors[index] = sorted((anchestors[index]))
        return anchestors