class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        INF = 10**18
        
        adj = defaultdict(list)
        
        for u,v,w in times:
            
            adj[u].append([v,w])
            
        dist = [INF]*(n+1)
        
        dist[k] = dist[0] = 0
        
        min_heap = list()
        
        heappush(min_heap, [0,k])
        
        vis = set()
        
        while min_heap:
            
            curr_weight, node = heappop(min_heap)
            
            if node in vis:
                
                continue
                
            vis.add(node)
            
            for adjacent, weight in adj[node]:
                
                if dist[adjacent] > curr_weight + weight:
                    
                    dist[adjacent] = curr_weight + weight
                    
                    heappush(min_heap,[curr_weight + weight, adjacent])
        print(dist)
        m = max(dist)
        return -1 if m == INF else m
