'''

[10,15,20]

[10,15,30]

[1,100,1,1,1,100,1,1,100,1]

[1,100,2,3,3,103,4,5,104,6]

'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * len(cost)
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,len(cost)):
            
            dp[i] = min(dp[i-1]+cost[i],dp[i-2]+cost[i])
        #print(dp)
        return min(dp[-1],dp[-2])
