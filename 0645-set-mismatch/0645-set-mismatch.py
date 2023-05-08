class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        dup =-1
        not_here = -1
        
        for i in range(0,len(nums)):

            x = abs(nums[i])
            
            # Already marked 
            
            if nums[x-1] < 0:
                
                dup  = x
            else:
                nums[x-1]  = - nums[x-1]
        
        for i in range(len(nums)):
            
            if nums[i]>0:

                not_here = i+1
                
        return [dup,not_here]
            
        
                
            
            
            
        
            