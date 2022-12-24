class Solution:
    def numTilings(self, n: int) -> int:
        
        mod = (10**9) + 7
        
        if n <3:
            return n
        
        dp = [0]*(4)
        
        dp[1] ,dp[2], dp[3] = 1,2,5
        
        for i in range(4,n+1):
            
            dp[-3],dp[-2],dp[-1] = dp[-2],dp[-1],(2*(dp[-1]))%mod + (dp[-3])%mod
            
            
        return dp[-1]%mod