class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        min_heap = list()
        
        for i in range(candidates):
            
            heappush(min_heap,[costs[i],i,1])
            
        j = len(costs)-1
        
        count = 0
        
        while i<j and count < candidates:
            
            heappush(min_heap,[costs[j],j,2])
            j -= 1
            count += 1
        
        ans = 0
        i += 1
        # print(i,j)
        for _ in range(k):
            
            ele,idx,part = heappop(min_heap)
            ans += ele
            # print(ele)
            if i<=j:
                if part == 2:
                    # j-=1
                    heappush(min_heap,[costs[j],j,2])
                    j -= 1
                else:
                    # i+= 1
                    heappush(min_heap,[costs[i],i,1])
                    i += 1
            # print(min_heap)
        return ans
                
            