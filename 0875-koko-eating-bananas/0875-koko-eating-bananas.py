class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if h < len(piles):
            
            return -1
        
        low = 1
        high = max(piles)
        
        def valid(mid):
            
            return sum(ceil(pile/mid) for pile in piles) <= h
        
        while low <= high:
            
            mid = (low + high)//2
            
            if valid(mid):
                
                high = mid - 1
                
            else:
                
                low = mid + 1
                
        return low