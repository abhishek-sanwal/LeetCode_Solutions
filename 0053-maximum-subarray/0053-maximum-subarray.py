class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0
        
        max_sum = -sys.maxsize
        
        
        for ele in nums:
            
            curr_sum = max(curr_sum + ele, ele)
            
            max_sum = max(max_sum, curr_sum)
            
        return max_sum