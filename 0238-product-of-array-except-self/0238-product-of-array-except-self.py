class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        suffix = [0]*len(nums)
        
        ans = [0]*len(nums)
        
        pref = 1
        suffix[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            
            suffix[i] = nums[i]*suffix[i+1]
        suffix.append(1)
        
        for i in range(len(nums)):
            
            ans[i] = suffix[i+1]*pref
            pref *= nums[i]
        
        return ans
            

            
        
        