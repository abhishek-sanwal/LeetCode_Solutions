class Solution:
    def numSquares(self, n: int) -> int:
        
        INF = 10**18

        dp = [INF]*(n+1)

        dp[1] = 1
        
        for i in range(2,n+1):

            rt = int(i**0.5)

            if rt * rt == i:

                dp[i] = 1

            else:
                for j in range(rt,0,-1):
                    dp[i] = min(dp[i], dp[j*j] + dp[i-(j*j)])

        return dp[n]
        
