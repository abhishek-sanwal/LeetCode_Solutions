class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        
        row = len(grid)
        col = len(grid[0])
        
        vis = [[False]*col for _ in range(row)]
        
        check = set()
        global count
        count = 0
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def is_boundary(i,j):
            
            return i == 0 or i== row-1 or j==0 or j==col-1
        
        def is_valid(i,j):
            
            return i > -1 and i < row and j < col and j>-1
        
        def dfs(grid,node):
            
            global count 
            x,y = node
            
            vis[x][y] = True
            
            for x1,y1 in directions:
                if is_valid(x+x1,y+y1) and not vis[x+x1][y+y1] and grid[x+x1][y+y1]==1:
                    
                    count+=1
                    dfs(grid,[x+x1,y+y1])
                    
            
            
        tot  = 0
        for i in range(row):
            
            if grid[i][0] ==1 and not vis[i][0]:

                    source = (i,0)
                    dfs(grid,source)
                    count+=1
            
            if grid[i][col-1] == 1 and not vis[i][col-1]:
                    source = (i,col-1)
                    dfs(grid,source)
                    count+=1
                    
            for j in range(col):
                if grid[0][j] ==1 and not vis[0][j]:

                    source = (0,j)
                    dfs(grid,source)
                    count+=1
                        
                if grid[row-1][j] ==1 and not vis[row-1][j]:
                    
                    source = (row-1,j)
                    dfs(grid,source)
                    count+=1
                
                if grid[i][j] ==1:
                    tot+=1
        print(tot,count)
        return tot -count


        
    