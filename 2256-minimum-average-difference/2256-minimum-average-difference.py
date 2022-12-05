    
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        s = sum(nums)
        
        prefix = 0
        min_idx = mini =  10**6
        
        for i in range(len(nums)-1):
            
            prefix += nums[i]
            
            s -=  nums[i]
            
            prefix_average = prefix//(i+1)
            
            suffix_average = s//(len(nums)-i-1) 
            
            if abs(prefix_average - suffix_average) < mini:
                
                mini = abs(prefix_average - suffix_average)
                min_idx = i
        prefix += nums[-1]
        if prefix//(len(nums)) < mini:
            mini = prefix 
            min_idx = len(nums)-1
        
        return min_idx