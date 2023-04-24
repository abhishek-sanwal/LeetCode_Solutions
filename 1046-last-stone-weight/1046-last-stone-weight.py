from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxheap = [-i for i in stones]
        
        heapify(maxheap)
        
        while len(maxheap)>1:
            
            a = -1*heappop(maxheap)
            b = -1*heappop(maxheap)
            
            if a==b:
                continue
            heappush(maxheap,-1*(a-b))
            
        return -1*maxheap[0] if maxheap else 0