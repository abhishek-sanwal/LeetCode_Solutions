class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0
        
        maxi = -math.inf
        
        for ele in nums:
            
            curr_sum = max(curr_sum + ele, ele)
            
            maxi = max(maxi,curr_sum)
            
        return maxi
    
        for i in range(len(nums)):
            
            sumi = 0
            
            for j in range(i,len(nums)):
                
                sumi += nums[j]
                
                maxi = max(maxi,sumi)
                
        return maxi