class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        vis = set()
        
        large = -1
        
        for element in nums:
            
            if -element in vis:
                    
                large = max(large,abs(element))
                
            if -element not in vis and element not in vis:
                vis.add(element)
                
                
        return large
            
            