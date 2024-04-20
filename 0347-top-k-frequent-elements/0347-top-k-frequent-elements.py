
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mapp = {}
        
        #0(N)
        for i in nums:
            
            mapp[i] = mapp.get(i,0) + 1
        
        bucket = [[] for i in range(len(nums)+1)]
        
        # Bucket sort on frequencies
        for i in mapp:
            
            bucket[mapp[i]].append(i)
            
        ans = list() 
        
        for i in range(len(bucket)-1,-1,-1):
            
            if bucket[i]:
                ans.extend(bucket[i])
            if len(ans) ==k:
                break
        return ans
            
        
        min_heap = []
        # 0(nlogk)
        for i in mapp:
            
            heappush(min_heap,[mapp[i],i])
            
            if len(min_heap) > k:

                heappop(min_heap)
        #0(n)
        return [i[1] for i in min_heap]
            
        