class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        INF = 10**18
        
        # Dp is our distane array it is 2d it represents distance between any two vertices.
        dp =[[ INF for i in range(n)] for j in range(n)]
        
        # mark source to source distance as zero.
        for source in range(0,n):
            
            dp[source][source] = 0 # Source to source distance is zero.
        
        # Stores edges in dp array[distance array]
        
        for source, destination, weight in edges:

            dp[source][destination] = weight
            
            dp[destination][source] = weight # For undirected edges
        
        #  Now apply floyd warshall algo
        for via_node in range(n):

            for source in range(n):

                for destination in range(n):
                    
                    dp[source][destination] = min(dp[source][destination], dp[source][via_node] + dp[via_node][destination])
        
        
        min_count = INF
        mini = -1
        
        # Iterate over all the cities source
        for source in range(n):
            
            count = 0
            
            # check wheather shorest path from source to destination is less than thresshold or not  
            for destination in range(n):
                
                if source != destination and dp[source][destination] <= distanceThreshold:

                    count += 1
        # Update min_count and source
            if count <= min_count:
                
                min_count = count
                mini = source
                
        return mini