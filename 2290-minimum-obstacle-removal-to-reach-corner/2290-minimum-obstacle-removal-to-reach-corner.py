class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        
        col = len(grid[0])
        
        directions = [ [1,0], [0,1], [-1,0], [0,-1] ]
        
        isValid = lambda x,y:x > -1 and x < row and y > -1 and y < col
        
        vis = set()
        
        def bfs():
            
            que = deque([ [0,0,0] ] )
            
            vis.add((0,0))
            
            while que:
                
                x,y,cost = que.popleft()
                
                if x==row-1 and y == col-1:
                    
                    return cost
                
                for x1,y1 in directions:
                
                    new_x, new_y = x + x1, y + y1
                    
                    
                    if isValid(new_x, new_y) and (new_x, new_y) not in vis:
                        
                        vis.add((new_x, new_y))
                        
                        if grid[new_x][new_y] == 0:
                            
                            que.appendleft( [new_x, new_y, cost] )
                            
                        else:
                            
                            que.append( [new_x, new_y, cost+1] )
                            
            
            return -1
        
        return bfs()
                
                
        
        flat = lambda x,y: x*col + y
        
        INF = 10**18
        
        dist = [INF]*(row * col)
        
        dist[0] = 0
        
        min_heap = list()
        
        vis = set()
        
        heappush(min_heap, [0,0])
        
        while min_heap:
            
            curr_weight, node = heappop(min_heap)
            
            if node in vis:
                
                continue
                
            vis.add(node)
            
            x,y = node // col, node % col
            
            for x1,y1 in directions:
                
                new_x, new_y = x + x1, y + y1
                
                curr_node = flat(new_x, new_y)
                
                if isValid(new_x, new_y) and dist[curr_node] > dist[node] + grid[new_x][new_y]:
                    
                    dist[curr_node] = dist[node] + grid[new_x][new_y]
    
                    heappush(min_heap,[dist[node] + grid[new_x][new_y], curr_node])
        
        
        print(dist)
        return dist[row*col-1]
