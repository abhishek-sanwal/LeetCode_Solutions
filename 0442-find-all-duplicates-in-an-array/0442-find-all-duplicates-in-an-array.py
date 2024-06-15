class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res = list()
        for x in nums:
            index = abs(x)-1    
            # Already marked index
            if nums[index] < 0:
                
                res.append(abs(x))
                
            # Mark the index
            else:
                nums[index] *= -1
        return res