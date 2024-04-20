
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mapp = {}
        
        for i in nums:
            
            mapp[i] = mapp.get(i,0) + 1
            
        max_heap = [ [-mapp[i],i] for i in mapp]
        heapify(max_heap)
        
        ans = []
        
        while k:
            
            ans.append(heappop(max_heap)[1])
            k-=1
            
        return ans
        