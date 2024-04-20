class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        [4,5,6,7,0,1,2]
        
        idx = 0
        for i in nums:
            
            if i == target:
                
                return idx
            
            idx += 1 
        
        return -1