class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        count = 0
        
        arr = sorted(heights)
        
        for i,j in zip(arr,heights):
            
            if i != j:
                
                count += 1
                
        return count