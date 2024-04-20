
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mapp = {}
        
        for i in nums:
            
            mapp[i] = mapp.get(i,0) + 1
            
        min_heap = []
        
        for i in mapp:
            
            heappush(min_heap,[mapp[i],i])
            
            if len(min_heap) > k:

                heappop(min_heap)
                
        return [i[1] for i in min_heap]
            
        