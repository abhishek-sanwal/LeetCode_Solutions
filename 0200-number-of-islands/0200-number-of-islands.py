class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = len(grid)
        
        col = len(grid[0])
        
        def isValid(i,j):
            
            return i>-1 and i< row and j>-1 and j<col
        
        directions = [
            [1,0],[0,1],[-1,0],[0,-1]
        ]
        
        vis = set()
        
        def dfs(x,y):
            
            vis.add((x,y))
            
            for x1,y1 in directions:
                
                new_x, new_y = x+x1,y+y1
                
                if isValid(new_x, new_y) and (new_x,new_y) not in vis and grid[new_x][new_y] == "1":
                    
                    dfs(new_x, new_y)
                
                    
            return None
        
        def bfs(x,y):
            
            que = deque([[x,y]])
            
            while que:
                
                for _ in range(len(que)):
                    
                    x,y = que.popleft()
                    
                    for x1,y1 in directions:

                        new_x, new_y = x+x1,y+y1

                        if isValid(new_x, new_y) and (new_x,new_y) not in vis and grid[new_x][new_y] == "1":

                            que.append([new_x, new_y])
                            vis.add((new_x, new_y))
                    
            return None
        
        count = 0
        
        for i in range(row):
            
            for j in range(col):
            
                if (i,j) not in vis and grid[i][j] =="1":
                    # print("called")
                    # dfs(i,j)
                    bfs(i,j)
                    count += 1
                    
        return count