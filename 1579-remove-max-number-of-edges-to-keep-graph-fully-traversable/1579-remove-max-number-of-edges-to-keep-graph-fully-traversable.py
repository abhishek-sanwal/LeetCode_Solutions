
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
        # print(self.distinct_components)
        return self.distinct_components == 1
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        alice = Unionfind(n)
        
        bob = Unionfind(n)
        
        count = 0
        
        edges.sort(key=lambda x:(-x[0]))
        
#         1 =>2 Alice and Bob
        
#         3 => 4 Alice and Bob
        
    
        for typ, source, dest in edges:
            
            
            if typ in [1,3]:
                
                areMerged1 = alice.Union(source, dest)
            
            if typ in [2,3]:
                
                areMerged2 = bob.Union(source, dest)
            
            
            count += int(areMerged1 if typ == 1 else ( areMerged2 if typ == 2 else areMerged1 & areMerged2 ))
        
        return -1 if not(alice.isUnited() and bob.isUnited()) else count
        
        
#         alice = defaultdict(list)
        
#         bob = defaultdict(list)
        
#         alice_edges = bob_edges = 0
        
#         # Created adjancey list for Alice and Bob         
        
#         for typ,u,v in edges:
            
#             if typ in [1,3]:
                
#                 alice[u].append(v)
#                 alice[v].append(u)
#                 alice_edges += 1
                
#             if typ in [2,3]:
                
#                 bob[u].append(v)
#                 bob[v].append(u)
                
#                 bob_edges += 1
             
#         alice
#         1 => 2
        
#         2 => 3
        
#         2 => 4
        
#         Bob
#         1=>2
        
#         2=> 3
        
        
                
                
                
                
        
        
# #         1 =>2 Alice and Bob
        
# #         2 => 3 Alice and Bob can go
        
#         1 => 3 Alice can go
        
#         2 => 4 Alice can go
        
#         1 => 2 Alice can go
        
#         3 => 4 bob can go
        
#         1 =>2
        
#         2=>3
        
#         2 => 4
        
#         2nd
        
#         1 =>2 Alice and Bob can go
        
#         2 => 3 Alice and Bob can go
        
#         1 => 4 Alice can go
        
#         1 => 4 Bob can go
        
        
#         [2,3] Alice and Bob
        
#         [1,4] Incoming edges I need to find 
        
        
        