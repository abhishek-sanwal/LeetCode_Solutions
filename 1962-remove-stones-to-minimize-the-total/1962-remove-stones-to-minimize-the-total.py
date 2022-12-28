from  heapq import heappop,heappush

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        maxheap = [-pile for pile in piles]
        
        heapify(maxheap)
        
        for _ in range(k):
            
            maxi = heappop(maxheap)
            
            heappush(maxheap,maxi//2)

        
        return sum(maxheap) *-1
        # since no pile can be negative we can do this.
        