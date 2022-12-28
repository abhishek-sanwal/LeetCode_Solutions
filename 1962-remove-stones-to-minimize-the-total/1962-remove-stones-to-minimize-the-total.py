from  heapq import heappop,heappush

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        maxheap = []
        
        for pile in piles:

            maxheap.append(-1*pile)
        
        heapify(maxheap)
        
        while k:
            
            maxi = heappop(maxheap)
            
            heappush(maxheap,maxi//2)
                
            k-=1
        
        return sum(maxheap) *-1
        # since no pile can be negative we can do this.
        