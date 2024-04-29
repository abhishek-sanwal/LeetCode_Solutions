class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not word or not board:
            
            return False
        
        row = len(board)
        col = len(board[0])
        
        up = [0,1]
        down = [0,-1]
        left = [-1,0]
        right = [1,0]
        
        directions = [up, down, left, right]
        
        def valid(x,y):
            
            return x>-1 and x<row and y>-1 and y<col
        
        def dfs(x,y,ptr,vis):
            vis.add((x,y))
            #print(x,y,ptr)
            if ptr == len(word):
                # We found a match 
                return True
            
            for x1,y1 in directions:
                
                new_x, new_y = x + x1, y + y1
                
                if valid(new_x, new_y) and board[new_x][new_y] == word[ptr]:
                    
                    if (new_x,new_y) not in vis:
                        if dfs(new_x, new_y, ptr+1,vis):
                            return True
                        vis.remove((new_x,new_y))
                        
            return False
        
        ptr = 0
        vis = set()
        for i in range(row):
            
            for j in range(col):
                
                if board[i][j] == word[ptr]:
                    vis.add((i,j))
                    if dfs(i,j,ptr + 1,vis):
                        
                        return True
                    vis.remove((i,j))
                    
        return False
                