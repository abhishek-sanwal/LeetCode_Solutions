
class Unionfind:
    
    def __init__(self,size):
        
        self.parent = [i for i in range((size)+1)]
        
        self.rank = [0] * ((size) + 1)
        
        self.distinct_components = size
        
    def find_parent(self,u):
        
        if u ==  self.parent[u]:
            
            return u
            
        self.parent[u] = self.find_parent(self.parent[u])
        
        return self.parent[u]
    
    def UnionParent(self,A,B):
        
        self.distinct_components -= 1
        if A != B:
            
            if self.rank[A] < self.rank[B]:
                A,B = B,A
                
            self.parent[B] = A
            
            if self.rank[A] == self.rank[B]:
                self.rank[A] += 1
                
        
    def Union(self,u,v):
        
        A = self.find_parent(u)
        B = self.find_parent(v)
        
        if A == B:
            
            # Already merged nodes
            return True
        
        self.UnionParent(A,B)

        return False
    
    def isUnited(self):
        return self.distinct_components == 1









class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        dsu = Unionfind(len(isConnected))
        
        for i in range(len(isConnected)):
            
            for j in range(len(isConnected[i])):
                
                if isConnected[i][j] == 1 and i != j:
                    
                    dsu.Union(i,j)
                    
        
        return dsu.distinct_components
        
        
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
        
        def bfs(node):
            
            que = deque([node])
            
            while que:
                
                for _ in range(len(que)):
                    
                    node = que.popleft()
                    
                    for adjacent in adj[node]:
                        
                        if adjacent not in vis:
                            
                            vis.add(adjacent)
                            que.append(adjacent)
                            
            return None
        
        
        
        
            
        count = 0
        for i in range(len(isConnected)):
            
            if i not in vis:
                
                # dfs(i)
                bfs(i)
                count += 1
                
        return count