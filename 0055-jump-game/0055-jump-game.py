class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxi = 0
        
        for i in range(len(nums)-1):
            
            if maxi < i:
                return False
            
            maxi = max(maxi,i+nums[i])
        
        return maxi >= len(nums)-1