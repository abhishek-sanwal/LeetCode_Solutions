class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        que = deque()
        
        row = len(grid)
        
        col = len(grid[0])
        
        def isValid(i,j):
            
            return i>-1 and i< row and j>-1 and j<col
        
        directions = [
            
            [1,0],
            [0,1],
            [-1,0],
            [0,-1]
        ]
        
        
        # Multi-source bfs         
        one_count = 0
        for i in range(row):
            
            for j in range(col):

                if grid[i][j] == 2:
                    
                    que.append([i,j])
                    
                elif grid[i][j] == 1:
                    
                    one_count += 1
                    
                    
        minutes = 0        
        while que:
            flag = False
            for i in range(len(que)):
                
                x,y = que.popleft()
                    
                for x1,y1 in directions:

                    new_x, new_y = x+x1,y+y1

                    if isValid(new_x, new_y) and grid[new_x][new_y] == 1:
                        
                        one_count -= 1
                        grid[new_x][new_y] = 2
                        flag = True
                        que.append([new_x, new_y])
                # print(grid)
            if flag:
                minutes  += 1  
        print(one_count)
        return minutes if not one_count else -1
                    
        