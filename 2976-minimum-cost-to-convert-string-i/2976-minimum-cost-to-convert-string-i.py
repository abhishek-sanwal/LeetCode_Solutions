class Solution:
    
    INF = 10**12
    
    def get_ascii_lowercase(self, char):
        
        return ord(char) - 97
    
    
    def find_shortest_distance(self, source, destination, adj):
        
        distance = [self.INF]*26
        
        pq = list()
        
        source = self.get_ascii_lowercase(source)
        destination = self.get_ascii_lowercase(destination)
        
        distance[source] = 0
        heappush(pq,[distance[source], source])
        
        vis = set()
        
        while pq:
            
            curr_weight, node = heappop(pq)
            
            if node in vis:
                continue
                
            vis.add(node)
            
            for adjacent, weight in adj[node]:
                
                if distance[node] + weight < distance[adjacent]:
                    
                    distance[adjacent] = distance[node] + weight
                    
                    heappush(pq,[distance[node] + weight, adjacent])
                    
        return distance[destination]
        
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        IMPOSSIBLE = -1
        
        cache = dict()
        
        if len(source) != len(target):
            
            return IMPOSSIBLE
        
        adj = defaultdict(list)
        
        for u,v,w in zip(original, changed, cost):
            u = self.get_ascii_lowercase(u)
            v = self.get_ascii_lowercase(v)
            adj[u].append([v,w])
        
        
        ans = 0
        
        for char1, char2 in zip(source, target):
            
            if (char1, char2) in cache:
                
                distance = cache[(char1, char2)]
            
            else:
            
                distance = self.find_shortest_distance(char1, char2, adj)
                cache[(char1, char2)] = distance
            
            if distance == self.INF:
                
                return IMPOSSIBLE
            
            ans += distance
        
        return ans
                
            
