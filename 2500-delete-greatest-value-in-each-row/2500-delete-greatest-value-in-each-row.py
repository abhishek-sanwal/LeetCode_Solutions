class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        ans = 0
        
        for i in range(len(grid)):
            
            grid[i].sort(reverse=True)
            
        
        for col in range(len(grid[0])):
            curr = 0
            
            for row in range(len(grid)):
                
                curr = max(curr,grid[row][col])
                
            ans+=curr
        
        return ans
            
            