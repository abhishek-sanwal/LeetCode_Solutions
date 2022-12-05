    
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        s = sum(nums)
        
        prefix = 0
        min_idx = mini =  10**6
        
        for i in range(len(nums)):
            
            prefix += nums[i]
            
            s -=  nums[i]
            
            prefix_average = prefix//(i+1)
            
            suffix_average = s//(len(nums)-i-1) if len(nums)-i-1 else 0
            
            if abs(prefix_average - suffix_average) < mini:
                
                mini = abs(prefix_average - suffix_average)
                min_idx = i
            #print(prefix_average,suffix_average,min_idx)
        return min_idx