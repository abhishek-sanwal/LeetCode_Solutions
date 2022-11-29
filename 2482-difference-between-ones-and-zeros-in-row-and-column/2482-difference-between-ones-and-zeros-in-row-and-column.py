class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        
        row = len(grid)
        
        col = len(grid[0])
        
        #mat =[[0]*col for i in range(row)]
        
        last_col_sum = 0
        
        for i in range(row):
            last_col_sum += grid[i][col-1]
        
        for i in range(row):
            row_sum = 0
            for j in range(col):
                row_sum += grid[i][j]
                if i>0:
                    grid[i][j] += grid[i-1][j]
                
            grid[i][j] = row_sum
        #print(grid)
        for i in range(row):
            for j in range(col):
                if j!= col-1:
                    grid[i][j] = grid[i][col-1] + grid[row-1][j] - (col - grid[i][col-1]) - (row -  grid[row-1][j])
                else:
                    grid[i][j] = grid[i][col-1] + last_col_sum - (col - grid[i][col-1]) - (row -  last_col_sum)
                    
        return grid
                