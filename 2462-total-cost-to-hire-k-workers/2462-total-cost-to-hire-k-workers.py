class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        min_heap = list()
        
        for i in range(candidates):
            
            heappush(min_heap,[costs[i],1])
            
        j = len(costs)-1
        
        count = 0
        
        while i<j and count < candidates:
            
            heappush(min_heap,[costs[j],2])
            j -= 1
            count += 1
        
        ans = 0
        # python loop variable takes end value of range         
        i += 1
        for _ in range(k):
            
            ele, part = heappop(min_heap)
            ans += ele
            if i<=j:
                if part == 2:
                    heappush(min_heap,[costs[j],2])
                    j -= 1
                else:
                    heappush(min_heap,[costs[i],1])
                    i += 1
            
        return ans
                
            