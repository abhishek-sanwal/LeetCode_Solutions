class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k<=1:
            
            return 0
        
        front = rear = 0
        
        prod = 1
        count = 0
        
        for rear in range(len(nums)):
            
            prod *= nums[rear]
                
            #Slide subarray to make it valid
            while prod >= k:

                prod //= nums[front]
                front += 1
                
            count += rear -front +1 
        return count
            
                

            