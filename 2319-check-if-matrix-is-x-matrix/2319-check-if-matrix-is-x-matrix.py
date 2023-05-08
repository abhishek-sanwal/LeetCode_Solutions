class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        
        n = len(grid)
        
        for i in range(len(grid)):
            
            for j in range(len(grid)):

                if i==j or (i + j + 1  == n):
                    
                    if not grid[i][j]:
                        print(i,j,grid[i][j])
                        return False
                
                elif grid[i][j]:
                    print(i,j,grid[i][j])
                    return False
        
        return True