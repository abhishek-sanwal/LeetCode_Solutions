class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        number = -1
        
        for i in range(len(nums)):
            
            if count == 0:
                number = nums[i]
                count = 1
                continue
                
            if nums[i] != number:
                count -= 1
            
            else:
                count += 1
                
            
        return number