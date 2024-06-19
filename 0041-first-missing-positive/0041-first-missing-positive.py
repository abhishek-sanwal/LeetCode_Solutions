class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        i = 0
        n = len(nums)
        
        while i < len(nums):
            idx = nums[i]-1
            if 0 < nums[i] <= n and nums[i] != nums[idx]:
                nums[i],nums[idx] = nums[idx], nums[i]
                
            else:
                i += 1
        
        for i in range(n):
            
            if nums[i] != i+1:
                
                return i+1
            
        return n+1