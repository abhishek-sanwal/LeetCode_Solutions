class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) ==1:
            return nums[0]
        
        arr = nums
        
        prev1 = curr1  = 0
        prev2 = curr2 = 0
        
        for i in range(len(nums)):
            
            if i>0:
                
                prev2,curr2 = curr2,max(curr2,prev2+nums[i])
            
            if i<len(nums)-1:
                
                prev1,curr1 = curr1,max(curr1,prev1 + nums[i])
        
        print(curr1,curr2)
        
        return max(curr1,curr2)