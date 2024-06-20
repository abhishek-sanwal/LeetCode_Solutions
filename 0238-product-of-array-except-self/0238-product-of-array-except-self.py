class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [0]*len(nums)
        
        pref = 1
        ans[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            
            ans[i] = nums[i]*ans[i+1]
        
        for i in range(len(nums)):
            
            ans[i] = (ans[i+1] if i< len(nums)-1 else 1 )*pref
            pref *= nums[i]
        return ans
            

            
        
        