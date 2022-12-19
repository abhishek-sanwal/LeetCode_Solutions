class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = [-1] * 40
        dp[0] = 0
        dp[1] = dp[2] =1
        
        # Topdown dp
        def topdown(n):
            
            nonlocal dp
            
            if dp[n] != -1:
                
                return dp[n]
            
            dp[n] = topdown(n-1) + topdown(n-2) + topdown(n-3)
            # Tn = Tn-1 + Tn-2 + Tn-3 for n >= 0.
            return dp[n]
        
        # bottomup dp
        def bottomup(n):
            
            nonlocal dp
            
            for i in range(3,n+1):
                
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            
            return dp[n]
        
                
        #bottomup(n)
        #topdown(n)
        #return dp[n]
        
        # No-dp each subproblem depends upon previous three subproblems
        
        if n==0:
            return 0
        
        x,y,z =1,1,0
        
        for i in range(3,n+1):
            x,y,z = x+y+z,x,y
            
        return x
            
        
        