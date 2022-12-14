class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = nums
        if len(nums) == 1:
            return nums[0]
        
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
            
            
        