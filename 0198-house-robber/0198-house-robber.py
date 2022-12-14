
'''

Fibonacci Relation

= > f(i) = f(i-1) + f(i-2)

House Robber Relation

 = > f(i) = max(f(i-1),f(i-2) + nums[i])

where,

    i represents index

so relation is dependent on only previous two results so we can just use two variables to have that result and keep on going to get result.

'''
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        arr = nums
        
        prev = curr  = 0
        
        for i in range(len(nums)):
            
            prev,curr = curr,max(curr,nums[i] + prev)
            
        return curr
        
        
        dp = [0]*len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,len(arr)):
            
            dp[i] = max(dp[i-1],arr[i]+dp[i-2])
            
        print(dp)
        return dp[-1]
            
            
        