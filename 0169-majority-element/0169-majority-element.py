class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 1
        number = nums[0]
        
        for i in range(1,len(nums)):
            
            if nums[i] != number:
                count -= 1
            
            else:
                count += 1
                
            if count == 0:
                number = nums[i]
                count = 1
                
        return number