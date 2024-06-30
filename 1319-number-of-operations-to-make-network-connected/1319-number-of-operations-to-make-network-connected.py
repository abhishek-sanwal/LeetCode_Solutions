
class Unionfind:
    
    def __init__(self,size):
        
        self.parent = [i for i in range((size))]
        
        self.rank = [0] * ((size))
        
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
        # print("hello")
        return False
    
    def isUnited(self):
        
        return self.distinct_components == 1
        
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        dsu = Unionfind(n)
        
        count = 0
        
        for source, dest in connections:
            
            areMerged = dsu.Union(source, dest)
            
            count += int(areMerged)
        # print(dsu.distinct_components,count)
        return -1 if dsu.distinct_components-1 > count else dsu.distinct_components-1
            
        
            