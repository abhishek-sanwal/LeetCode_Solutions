from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        #[i-1][j] + [i] [j-1]
        row,col = m,n
        
        #dp = [[0 for i in range(col)] for j in range(row)]
        
        # Previous row [i-1]
        dp = [1 for i in range(col+1)]
        
        # Current row[i]
        
        new_dp = [1 for i in range(col+1)]
        
        for i in range(1,row):
            
            for j in range(1,col):
                
                new_dp[j] = dp[j] + new_dp[j-1]
                
            print(new_dp)    
            dp = new_dp[:]
            
        
        return new_dp[-2]
        
        
        for i in range(row):
            
            dp[i][0] = 1
        
        for j in range(col):
            
            dp[0][j] = 1
        
        for i in range(1,row):
            
            for j in range(1,col):
                
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        return dp[-1][-1]
                
                
        
        def isValid(i,j):

            return i>-1 and i<n and j>-1 and j<m
        
        def recursion(i,j):
            
            if isValid(i,j):
                
                if i==n-1 and j==m-1:
                    return 1
                
                return recursion(i+1,j) + recursion(i,j+1)
            
            return 0
        
        return recursion(0,0)