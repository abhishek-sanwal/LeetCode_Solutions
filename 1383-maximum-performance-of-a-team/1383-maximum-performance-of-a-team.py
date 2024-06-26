class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        nums2 = efficiency
        nums1 = speed
        
        temp = [[nums2[i],nums1[i]] for i in range(len(nums2))]
        
        temp.sort(key=lambda x:-x[0])
        # print(temp)
        min_heap = list()
        
        sumi = ans =  0
        mod = (10**9) + 7
        for i in range(len(temp)):
            
            heappush(min_heap, temp[i][1])
            sumi += temp[i][1]
            if len(min_heap) > k:
                
                sumi -=heappop(min_heap)
            
            ans = max(ans, (sumi*temp[i][0]))
            
        return ans%mod
        