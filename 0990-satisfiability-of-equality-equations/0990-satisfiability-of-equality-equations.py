
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
    def equationsPossible(self, equations: List[str]) -> bool:
        
        dsu = Unionfind(26)
        
        not_equal = set()
        
        for var1,opr,_,var2 in equations:
            
            var1 = ord(var1)- ord('a')
            var2 = ord(var2)- ord('a')
            
            # Merge operation
            if opr == "=":
                
                dsu.Union(var1, var2)
                
        for var1,opr,_,var2 in equations:
            
            if opr == "!":
                var1 = ord(var1)- ord('a')
                var2 = ord(var2)- ord('a')

                if dsu.find_parent(var1) == dsu.find_parent(var2):

                    return False
        return True
                
            
                
                
            
            
            
            
        
        
        pass
       