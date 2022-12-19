
#ways(n) = {n: for i in [0-3] else ways(n-1) + ways(n-2)}

class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1]*(46)
        dp[0] = dp[1] = 1
        # Top_down Dp
        # Memorization
        # Memorize the recursion call in lookup table dp
        # Start from higher subproblem to smaller
        def TopDown(n):
            
            nonlocal dp
            
            if n==0:

                return 1
            
            if n<0:
                return 0
            
            if dp[n] !=-1:
                
                return dp[n]
            
            dp[n] = TopDown(n-1) + TopDown(n-2)
            
            return dp[n]
        
        # BottomUp dp
        # Start from smaller subproblem to larger subproblem
        
        def BottomUp(n):
            
            nonlocal dp
    
            for i in range(2,n+1):

                dp[i] = dp[i-1] + dp[i-2]
            
            return dp[n]
        TopDown(n)
        # BottomUp(n)
        return dp[n]
        
        x,y = 1,1
        
        # ways(n) = ways(n-2) + ways(n-1)
        
        # No dp since only previous two results we need for every ways(n)
        for i in range(2,n+1):
            
            x,y = x+y,x
            
        return x
        
        
        