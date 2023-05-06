class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        front  = 0
        
        mini = 10**12
        curr = 0
        
        for rear in range(0,len(nums)):
            
            curr += nums[rear]
            
            while curr >= target:
                
                mini = min(mini,rear-front+1)
                curr -= nums[front]
                front += 1
                
        
        return mini if mini != 10**12 else 0
            
            
            