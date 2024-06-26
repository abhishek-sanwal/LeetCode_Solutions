class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        # I need to find kth min element in nums2:
       
#         0 max element => n min element
        
#         (n-k) max element ko remove kru
        
#         n-k max element kth min element
#         total = res = 0
#         h = []
#         for a,b in sorted(list(zip(A, B)), key=lambda ab: -ab[1]):
#             heappush(h, a)
#             total += a
#             if len(h) > k:
#                 total -= heappop(h)
#             if len(h) == k:
#                 res = max(res, total * b)
#         return res
    
        temp = [[nums2[i],nums1[i]] for i in range(len(nums2))]
            
        temp.sort(key=lambda x:-x[0])
        
        min_heap = list()
        
        sumi = ans =  0
        
        for i in range(len(temp)):
            
            heappush(min_heap, temp[i][1])
            sumi += temp[i][1]
            # print(min_heap,sumi)
            if len(min_heap) > k:
                
                sumi -=heappop(min_heap)
            
            if len(min_heap) == k:
                # print(sumi,min_heap)
                ans = max(ans, sumi*temp[i][0])
            
        return ans
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        temp = [[nums2[i],i] for i in range(len(nums2))]
        
        temp.sort(reverse=True)
        
        sumi = 0
        
        for i in range(k):
            
            sumi += nums1[temp[i][1]]
            
        ans = sumi * temp[k-1][0]
        print(sumi,temp)
        [1,2,3,4]
        [3,1,3,2]
        [4,3,2,1]
        [2,3,1,3]
        
        [13,11,7,6]
        [14,2,1,12]
        
        
        
        for i in range(k,len(temp)):
            
            sumi -= nums1[temp[i-k][1]]
            sumi += nums1[temp[i][1]]
            print(sumi,temp[i][0])
            ans = max(ans,sumi * temp[i][0])
            
        return ans