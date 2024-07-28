class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        
        col = len(grid[0])
        
        directions = [ [1,0], [0,1], [-1,0], [0,-1] ]
        
        isValid = lambda x,y:x > -1 and x < row and y > -1 and y < col
        
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
                # print(curr_node, new_x, new_y,len(dist),new_x*row + new_y)
                if isValid(new_x, new_y) and dist[curr_node] > dist[node] + grid[new_x][new_y]:
                    
                    dist[curr_node] = dist[node] + grid[new_x][new_y]
    
                    heappush(min_heap,[dist[node] + grid[new_x][new_y], curr_node])
        
        
        print(dist)
        return dist[row*col-1]
