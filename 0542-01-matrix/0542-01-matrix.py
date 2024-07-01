class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        grid = mat
        
        row = len(grid)
        
        col = len(grid[0])
        
        def isValid(i,j):
            
            return i>-1 and i< row and j>-1 and j<col
        
        directions = [
            [1,0],[0,1],[-1,0],[0,-1]
        ]
        
        que = deque()
        vis = set()
        
        ans = [[0 for i in range(col)] for j in range(row)]
        
        for i in range(row):
            
            for j in range(col):
                
                if grid[i][j] == 0:
                    
                    que.append([i,j])
                    ans[i][j] = 0
                    
                else:
                    # Mark unvisited
                    grid[i][j] = -1
                    
        
        mins = 1
        while que:
            
            for _ in range(len(que)):

                x,y = que.popleft()
                
                for x1,y1 in directions:
                    
                    new_x, new_y = x+x1, y+y1
                    
                    if isValid(new_x, new_y) and grid[new_x][new_y] == -1:
                        # print(new_x, new_y)
                        grid[new_x][new_y] = 1
                        ans[new_x][new_y] = mins
                        que.append([new_x, new_y])
                        
            mins += 1        
        print(grid)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        [[0,1,0,1,1],
         [1,1,0,0,1],
         [0,0,0,1,0],
         [1,0,1,1,1],
         [1,0,0,0,1]]
        
        def dfs(x,y,count):
            
            vis.add((x,y))
            
            if grid[x][y] == 0:
                
                return count
            
            mini = 10**18
            
            for x1,y1 in directions:
                
                new_x, new_y = x + x1, y + y1
                
                if isValid(new_x, new_y) and (new_x, new_y) not in vis:
                    
                    mini = min(mini, dfs(new_x, new_y, count+1))
            
            ans[x][y] = mini-count
            
            return mini
                        
        count = 0
        
        for i in range(row):
            
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in vis:
                    dfs(i,j,0)
        return ans